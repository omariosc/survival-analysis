# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import torch
# import numbers
# import warnings

import numpy
# from scipy.linalg import solve
# from sklearn.base import BaseEstimator
# from sklearn.exceptions import ConvergenceWarning
# from sklearn.utils.validation import check_array, check_is_fitted

# from ..base import SurvivalAnalysisMixin
# from ..functions import StepFunction
# from ..nonparametric import _compute_counts
# from ..util import check_arrays_survival


class CoxPHOptimizer:
    """Negative partial log-likelihood of Cox proportional hazards model"""

    def __init__(self, X, event, time, alpha, ties):
        # sort descending
        o = numpy.argsort(-time, kind="mergesort")
        self.x = torch.tensor(X[o, :], dtype=torch.float)
        self.event = event[o]
        self.time = time[o]
        self.alpha = alpha
        self.no_alpha = numpy.all(
            self.alpha < numpy.finfo(self.alpha.dtype).eps)
        if ties not in ("breslow", "efron"):
            raise ValueError("ties must be one of 'breslow', 'efron'")
        self._is_breslow = ties == "breslow"
        self.hessian = None
        self.gradient = None

    def nlog_likelihood(self, w):
        """Compute negative partial log-likelihood

        Parameters
        ----------
        w : array, shape = (n_features,)
            Estimate of coefficients

        Returns
        -------
        loss : float
            Average negative partial log-likelihood
        """
        time = self.time
        n_samples = self.x.shape[0]
        breslow = self._is_breslow
        xw = self.x@w

        loss = 0
        risk_set = 0
        k = 0
        while k < n_samples:
            ti = time[k]
            numerator = 0
            n_events = 0
            risk_set2 = 0
            while k < n_samples and ti == time[k]:
                if self.event[k]:
                    numerator = numerator + xw[k]
                    risk_set2 = risk_set2 + torch.exp(xw[k])
                    n_events = n_events + 1
                else:
                    risk_set = risk_set + torch.exp(xw[k])
                k = k + 1

            if n_events > 0:
                if breslow:
                    risk_set = risk_set + risk_set2
                    loss = loss - (numerator - n_events *
                                   torch.log(risk_set)) / n_samples
                else:
                    numerator = numerator/n_events
                    for _ in range(n_events):
                        risk_set = risk_set + risk_set2 / n_events
                        loss = loss - \
                            (numerator - torch.log(risk_set)) / n_samples

        # add regularization term to log-likelihood
#        return loss + torch.sum(self.alpha * torch.square(w)) / (2. * n_samples)
        return loss

    def update(self, w, offset=0):
        """Compute gradient and Hessian matrix with respect to `w`."""
        time = self.time
        x = self.x
        breslow = self._is_breslow
        exp_xw = numpy.exp(offset + numpy.dot(x, w))
        n_samples, n_features = x.shape

        gradient = numpy.zeros((1, n_features), dtype=w.dtype)
        hessian = numpy.zeros((n_features, n_features), dtype=w.dtype)

        inv_n_samples = 1. / n_samples
        risk_set = 0
        risk_set_x = numpy.zeros((1, n_features), dtype=w.dtype)
        risk_set_xx = numpy.zeros((n_features, n_features), dtype=w.dtype)
        k = 0
        # iterate time in descending order
        while k < n_samples:
            ti = time[k]
            n_events = 0
            numerator = 0
            risk_set2 = 0
            risk_set_x2 = numpy.zeros_like(risk_set_x)
            risk_set_xx2 = numpy.zeros_like(risk_set_xx)
            while k < n_samples and ti == time[k]:
                # preserve 2D shape of row vector
                xk = x[k:k + 1]

                # outer product
                xx = numpy.dot(xk.T, xk)

                if self.event[k]:
                    numerator += xk
                    risk_set2 += exp_xw[k]
                    risk_set_x2 += exp_xw[k] * xk
                    risk_set_xx2 += exp_xw[k] * xx
                    n_events += 1
                else:
                    risk_set += exp_xw[k]
                    risk_set_x += exp_xw[k] * xk
                    risk_set_xx += exp_xw[k] * xx
                k += 1

            if n_events > 0:
                if breslow:
                    risk_set += risk_set2
                    risk_set_x += risk_set_x2
                    risk_set_xx += risk_set_xx2

                    z = risk_set_x / risk_set
                    gradient -= (numerator - n_events * z) * inv_n_samples

                    a = risk_set_xx / risk_set
                    # outer product
                    b = numpy.dot(z.T, z)

                    hessian += n_events * (a - b) * inv_n_samples
                else:
                    numerator /= n_events
                    for _ in range(n_events):
                        risk_set += risk_set2 / n_events
                        risk_set_x += risk_set_x2 / n_events
                        risk_set_xx += risk_set_xx2 / n_events

                        z = risk_set_x / risk_set
                        gradient -= (numerator - z) * inv_n_samples

                        a = risk_set_xx / risk_set
                        # outer product
                        b = numpy.dot(z.T, z)

                        hessian += (a - b) * inv_n_samples

        if not self.no_alpha:
            gradient += self.alpha * inv_n_samples * w

            diag_idx = numpy.diag_indices(n_features)
            hessian[diag_idx] += self.alpha * inv_n_samples

        self.gradient = gradient.ravel()
        self.hessian = hessian

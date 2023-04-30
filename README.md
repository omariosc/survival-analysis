# Survival Analysis with Neural Networks

This repository contains the code for the paper `Survival Analysis with Neural Networks for Chronic Heart Failure Patients`.

## Summary

In this project, we investigated using a range of different neural network models in statistical models to examine associations of covariates from clinical data of an inhomogeneous population of *1,802 chronic heart failure* patients in the *UK-HEART2* cohort for *survival analysis*. These neural networks were used within a *partial-likelihood* acting as a *loss function* in reimplementing the *Cox Proportional-Hazards Optimizer* in `scikit-survival` combined with *CoxNNet* `(Ching et al., 2018)` to examine the *relationships* of covariates and estimate a *risk score* for a patient, given their covariates.

We successfully reimplemented *latent class analysis* using *Gaussian mixture models* with the *KMeans* algorithm and trained a neural network model for each class. The best of these models achieved a *c-statistic score* of `0.68` using `4` subgroups compared to `0.84` using *latent class regression* and `0.68` using standard *Cox Proportional-Hazards regression* `(Mbotwa et al., 2021)`.

We extensively explored different neural network solutions by modifying the *network architecture*, parameters such as the *learning rate* and *epochs*, and completely different solutions using *convolutional neural networks* in which we transformed patient data into an image where each pixel represented a covariate.

## Running Experiments

All code can be accessed via the [GitHub repository](https://github.com/omariosc/survival-analysis).

Reproducibility is possible by:

```bash
git clone https://github.com/omariosc/survival-analysis

pip install -r requirements.txt
```

The following interactive Python notebook can be run: `code.ipynb`.

Alternatively, the notebook and dataset can be imported into [Google Colaboratory](https://colab.research.google.com/). If there are issues with installing requirements, then this method should be used. However, it can take a few hours to run the entire notebook.

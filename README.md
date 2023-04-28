# Survival Analysis with Neural Networks

This repository contains the code for the paper `Survival Analysis with Neural Networks for Chronic Heart Failure Patients`.

## Summary

In this project, we investigated using a range of different neural network models in statistical models to examine associations of covariates from clinical data of an inhomogeneous population of 1,802 Chronic Heart Failure patients in the UK-HEART2 cohort for Survival Analysis. These neural networks were used within a partial-likelihood acting as a loss function in reimplementing the Cox Proportional-Hazards Optimizer in scikit-survival combined with CoxNNet (Ching et al., 2018) to examine the relationships of covariates and estimate a risk score for a patient, given their covariates.

We successfully reimplemented Latent Class Analysis using Gaussian Mixture Models with the KMeans algorithm and trained a neural network model for each class. The best of these models achieved a c-statistic score of 0.68 using 4 subgroups compared to 0.84 using Latent Class Regression (Mbotwa et al., 2021) and 0.68 using standard Cox Proportional-Hazards regression (Mbotwa et al., 2021).

We extensively explored different neural network solutions by modifying the network architecture, parameters such as the learning rate and epochs, and completely different solutions using Convolutional Neural Networks in which we transformed patient data into an image where each pixel represented a covariate.

## Introduction

Survival time analysis is a tool for analysing the expected time duration until one event occurs; used in many contexts, including credit risk, mechanical failure, criminal recidivism, divorce, childbearing, unemployment, and graduation from school (Fox, 2014). This project will focus on the prototypical event – expected duration until death.

A neural network is a machine learning model inspired by the structure and function of the human brain (Giunchiglia et al., 2018). Interconnected nodes, or “neurons”, process information and make predictions. A neural network is trained using a large dataset and an optimisation algorithm, which minimises the error between the predicted and actual outputs. The trained neural network can then make predictions on new, unseen data. They have proven highly effective in solving complex problems and are a crucial artificial intelligence component.

Neural networks can be used in survival analysis to model the relationship between various covariates (such as medical history, whether one has diabetes and treatment details, including the value of haemoglobin in one’s blood) and the time of an event of interest (such as death) (Yin et al., 2022). A neural network can learn non-linear relationships between predictors and the outcome and manage substantial amounts of data with many predictors. This makes it a powerful tool for survival analysis, where traditional statistical methods may struggle to model complex relationships.

This project explores using neural network models to examine associates of covariates from clinical data of an inhomogeneous population of chronic heart failure patients to produce a risk score for a patient given their covariates. This score can be used to estimate if a patient is more likely to survive than another. The aim is to see if neural networks, given their non-parametric and non-linear nature, can identify patterns and make predictions, including with other established methods, that traditional techniques cannot in the context of survival analysis.

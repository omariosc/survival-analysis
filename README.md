# Survival Analysis with Neural Networks

This repository contains the code for the future paper `Survival Analysis with Neural Networks for Chronic Heart Failure Patients`.

## Summary

In this project, we investigated using a range of different neural network models in statistical models to examine associations of covariates from clinical data of an inhomogeneous population of 1,802 chronic heart failure patients in the UK-HEART2 cohort for survival analysis. These neural networks were used within a partial-likelihood acting as a loss function in reimplementing the Cox Proportional-Hazards Optimizer in scikit-survival combined with CoxNNet (Ching et al., 2018) to estimate the coefficients of covariates and which of a pair of patients is more likely to survive than the other. The best of the final produced models achieved a median c-statistic score of 0.91 compared to 0.86 using latent class regression (Mbotwa et al., 2021) and 0.68 using standard Cox Proportional-Hazards regression (Mbotwa et al., 2021).

## Introduction

Survival time analysis is a tool for analysing the expected time duration until one event occurs; used in many contexts, including credit risk, mechanical failure, criminal recidivism, divorce, childbearing, unemployment, and graduation from school (Fox, 2014). This project will focus on the prototypical event – expected duration until death.

A neural network is a machine learning model inspired by the structure and function of the human brain. Interconnected nodes, or neurons" process information and make predictions. A neural network is trained using a large dataset and an optimisation algorithm, which minimises the error between the predicted and actual outputs. The trained neural network can then make predictions on new, unseen data. They have proven highly effective in solving complex problems and are a crucial artificial intelligence component.

Neural networks can be used in survival analysis to model the relationship between various covariates (such as medical history, whether one has diabetes and treatment details, including the value of haemoglobin in one’s blood) and the time of an event of interest (such as death). A neural network can learn non-linear relationships between predictors and the outcome and manage substantial amounts of data with many predictors. This makes it a powerful tool for survival analysis, where traditional statistical methods may struggle to model complex relationships.

This project explores using neural network models to examine associates of covariates from clinical data of an inhomogeneous population on chronic heart failure patients to predict if a patient is more or less likely to survive than another. The aim is to see if neural networks, given their non-parametric and non-linear nature, can identify patterns and make predictions that traditional techniques cannot in the context of survival analysis.

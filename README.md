# Survival Analysis with Neural Networks

This repository contains the code for the future paper `Survival Analysis with Neural Networks`.

## Summary

In this project, we will investigate the use of neural networks in statistical models used to examine associations between the survival time of an inhomogeneous population of chronic heart failure patients for survival analysis. This will involve using clinical data from 1,802 heart failure patients enrolled in the UK-HEART2 cohort. The goal is to see if neural networks can automatically discover sets of subclasses patients may belong to, with different properties affecting survivability.

## Introduction

Survival time analysis is a tool for analysing the expected time duration until one event occurs. This can be used in many contexts, including criminal recidivism, divorce, child-bearing, unemployment and graduation from school. This project will focus on the prototypical event – expected duration until death.

A neural network is a machine learning model inspired by the structure and function of the human brain. Interconnected nodes, or "neurons," process information and make predictions. A neural network is trained using a large dataset and an optimisation algorithm, which minimises the error between the predicted and actual outputs. The trained neural network can then make predictions on new, unseen data. They have proven very effective in solving complex problems and are a crucial artificial intelligence component.

Neural networks can be used in survival analysis to model the relationship between various predictors (such as medical history and treatment details) and the time of an event of interest (such as death).

A neural network can learn non-linear relationships between predictors and the outcome and handle large amounts of data with many predictors. This makes it a powerful tool for survival analysis, where traditional statistical methods may struggle to model complex relationships.

This project uses neural networks for subgroup discovery in survival analysis. The aim is to identify features within subgroups of patients resulting in different survival properties. Neural networks can learn these patterns and predict a patient’s subgroup.

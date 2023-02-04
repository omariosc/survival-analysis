# Survival Analysis with Neural Networks

This repository contains the code for the future paper `Survival Analysis with Neural Networks`.

## Summary

In this project, we investigated the use of neural networks to model survival functions for statistical models, used to examine associations between the survival time of patients for survival analysis. These neural networks were used to automatically discover sets of subclasses patients may belong to, with different survival properties affecting survivability.

We successfully reimplemented latent class analysis (complex models for survival analysis) to fit an inhomogeneous population of chronic heart failure patients. We compared the effectiveness of various survival functions, including extensively evaluating whether implemented models adequately represented the data using statistical diagnostics.

## Introduction

Survival analysis is a tool that studies the time between events – analysing the expected time duration until such an event occurs. There are many applications of survival analysis, including criminal recidivism, divorce, child-bearing, unemployment, graduation, repayment and more. This project focuses on the prototypical event – the expected duration until death. By considering the time between the entry of a patient to a study and a subsequent occasion, either death, a patient leaving the trial or the end of the study, we can make predictions about survival rates.

We can use models to investigate associations between the survival time of patients. These models use survival functions – tools used to represent the distribution of survival time by producing probabilities that a patient belongs to a set of subclasses affecting survival. Using neural networks, a type of artificial intelligence, it is possible that within a patient population, we can discover patients and groups of patients with different survival properties, which make them more or less likely to survive, by producing probabilities that a patient belongs to such sets of subclasses affecting survival.

This project will explore using such neural networks, amongst other established, well-researched techniques, to make predictions about the chances of survival of new patients. These techniques are used to estimate survival functions – the tool used to represent the distribution of survival time in these models – and to automatically discover sets of subclasses of different survival properties a patient may belong to, which affect survivability.

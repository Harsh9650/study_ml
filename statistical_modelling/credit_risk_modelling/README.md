# Notebook Order & Guide

This folder contains a small pipeline of notebooks. Run them **in order** from 1 → 5. Python file 
`hepler_functions.py` contains the helper functions used along the project.

> Filenames below are linked exactly as they exist (spelling preserved).

---

## Execution Order

1. **[Data_Exploarttion.ipynb](Data_Exploarttion.ipynb)**  
   Initial exploratory data analysis (EDA): shape, types, missingness, basic distributions, and quick visuals.

2. **[Data_Preprocessing_Cleaning.ipynb](Data_Preprocessing_Cleaning.ipynb)**  
   Data cleaning & preprocessing: missing-value handling, outlier treatment, encoding strategy selection, train/validation split, and feature sanity checks.

3. **[Classing_Discrete_Variables.ipynb](Classing_Discrete_Variables.ipynb)**  
   Grouping/binning of **categorical** predictors (e.g., rare label bundling, WOE-style groupings if applicable).

4. **[Classing_Continous_Variables.ipynb](Classing_Continous_Variables.ipynb)**  
   Binning of **continuous** predictors (quantile bins, monotonic binning/WOE-style classing, or domain-driven cut points).

5. **[Probability_of_Default_Model.ipynb](Probability_of_Default_Model.ipynb)**  
   Model development for PD: feature set assembly, model training, performance metrics (AUC, KS, PSI if relevant), calibration, and validation.

---

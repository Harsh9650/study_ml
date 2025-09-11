# Notebook Order & Guide

This folder contains a small pipeline of notebooks. Run them **in order** from 1 → 5. Python file 
`helper_functions.py` contains the helper functions used along the project.

---

## Execution Order

1. **[data_exploartion.ipynb](data_exploartion.ipynb)**  
   Initial exploratory data analysis (EDA): shape, types, missingness, basic distributions, and quick visuals.

2. **[data_preprocessing_cleaning.ipynb](data_preprocessing_cleaning.ipynb)**  
   Data cleaning & preprocessing: missing-value handling, outlier treatment, encoding strategy selection, train/validation split, and feature sanity checks.

3. **[classing_discrete_variables.ipynb](classing_discrete_variables.ipynb)**  
   Grouping/binning of **categorical** predictors (e.g., rare label bundling, WOE-style groupings if applicable).

4. **[classing_continous_variables.ipynb](classing_continous_variables.ipynb)**  
   Binning of **continuous** predictors (quantile bins, monotonic binning/WOE-style classing, or domain-driven cut points).

5. **[probability_of_default_model.ipynb](probability_of_default_model.ipynb)**  
   Model development for PD: feature set assembly, model training, performance metrics (AUC, KS, PSI if relevant), calibration, and validation.

---

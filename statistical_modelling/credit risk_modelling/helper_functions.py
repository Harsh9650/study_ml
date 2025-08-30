import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from dateutil.relativedelta import relativedelta

sns.set()

# Now, we will Define a function to compute the time difference in months, rounding up if days >= 15
def months_between(start_date, end_date):
    if pd.isna(start_date):
        return 0
    rd = relativedelta(end_date, start_date)
    months = rd.years * 12 + rd.months
    if rd.days >= 15:
        months += 1
    return months


def calculate_IV(train_input_dataset, train_output_dataset, variable_name, dtype = "Discrete"):

    sample_df  = pd.concat([train_input_dataset[variable_name], train_output_dataset], axis = 1) 

    # Define clear variable names
    category_col = sample_df.columns[0]   # 'grade'
    target_col = sample_df.columns[1]  

    # Count number of observations per category
    obs_per_category = sample_df.groupby(category_col, as_index=False)[target_col].count()
    
    # Compute mean of target column per category (i.e., proportion of good loans)
    mean_per_category = sample_df.groupby(category_col, as_index=False)[target_col].mean()
    
    # Rename for clarity
    obs_per_category.rename(columns={target_col: 'n_obs'}, inplace=True)
    mean_per_category.rename(columns={target_col: 'prop_good'}, inplace=True)
    
    # Calculate proportion of total observations for each category
    obs_per_category['prop_obs'] = obs_per_category['n_obs'] / obs_per_category['n_obs'].sum()
    
    # Estimate number of good and bad loans per category
    obs_per_category['n_good'] = mean_per_category['prop_good'] * obs_per_category['n_obs']
    obs_per_category['n_bad'] = obs_per_category['n_obs'] - obs_per_category['n_good']
    
    # Calculate the share of total good and bad loans per category
    obs_per_category['prop_good_total'] = obs_per_category['n_good'] / obs_per_category['n_good'].sum()
    obs_per_category['prop_bad_total'] = obs_per_category['n_bad'] / obs_per_category['n_bad'].sum()
    
    # Merge mean values back for completeness
    sample_df = pd.merge(obs_per_category, mean_per_category, on=category_col)
    
    # Caclculating Weight of Evidence (WoE)
    
    epsilon = 1e-10 # to avoid edge cases, where either prop_good_total or prop_bad_total is zero.
    
    sample_df['WOE'] = np.log((sample_df['prop_good_total'] + epsilon) / (sample_df['prop_bad_total'] + epsilon))

    if dtype == "Discrete":
        sample_df.sort_values(by='WOE', inplace=True) 
        sample_df.reset_index(drop = True)
    
    # Information value.
    sample_df['IV'] = (sample_df['prop_good_total'] - sample_df['prop_bad_total']) * sample_df['WOE']
    
    total_IV = sample_df['IV'].sum()
    print(f"Information Value (IV) for variable {variable_name}: {total_IV:.4f}")

    return sample_df, total_IV



def plot_by_woe(df_woe, rotation_of_x_axis_labels=0):
    '''The function below takes a DataFrame and an optional rotation
    angle for x-axis labels. It creates a line plot of WoE values.'''
    
    x = np.array(df_woe.iloc[:, 0].apply(str))
    # Converts the first column values to strings and stores them in array `x`.

    y = df_woe['WOE']
    # Extracts the 'WOE' column and assigns it to `y`.

    plt.figure(figsize=(18, 6))
    # Creates a figure of size 18 (width) x 6 (height).

    plt.plot(x, y, marker='o', linestyle='--', color='k')
    # Plots a line chart with circles as markers, dashed lines, and black color.

    plt.xlabel(df_woe.columns[0])
    # Sets x-axis label using the name of the first column.

    plt.ylabel('Weight of Evidence')
    # Sets y-axis label.

    plt.title(f'Weight of Evidence by {df_woe.columns[0]}')
    # Sets plot title dynamically based on the first column name.

    plt.xticks(rotation=rotation_of_x_axis_labels)
    # Rotates x-axis labels by the specified angle.
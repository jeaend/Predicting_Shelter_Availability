import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from scipy.stats import chi2_contingency


def all_days_present(num_uniqes_dates ,start_year, start_month, start_day, end_year, end_month, end_day):
    start_date = datetime(start_year, start_month, start_day)
    end_date = datetime(end_year, end_month, end_day) 

    # Calculate the number of days
    num_days = (end_date - start_date).days + 1 
    
    return num_days == num_uniqes_dates

# extends describe by mode and range
def extended_describe(df):
    # Describe the DataFrame
    df_description = df.describe().T
    # Calculate mode for each column
    mode_values = df.mode().iloc[0]
    df_description['mode'] = mode_values
    # Calculate range for each column
    range_values = df.max() - df.min()
    df_description['range'] = range_values
    return df_description

def print_correlation_matrix(df):
    cm = df.corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix')
    return plt.show()

# displays boxplot and coutplot side by side for specified feature
def plot_boxplot_and_countplot(df, feature):
   
    # create subplots
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # boxplot
    sns.boxplot(x=df[feature], ax=axes[0])
    axes[0].set_title('Box Plot of ' + feature)
    axes[0].set_xlabel(feature)

    # histplot
    sns.histplot(x=df[feature], ax=axes[1])
    axes[1].set_title('Count Plot of ' + feature)
    axes[1].set_xlabel(feature)

    plt.tight_layout()
    plt.show()

def plot_categorical_features(df):
    # Determine the number of rows needed based on the number of columns
    num_columns = len(df.columns)
    num_rows = (num_columns + 2) // 3  # Add 2 to round up to the nearest multiple of 3

    # Create subplots
    fig, axes = plt.subplots(num_rows, 3, figsize=(15, 5*num_rows))
    axes = axes.flatten()

    # Plot each categorical variable
    for i, column in enumerate(df.columns):
        sns.countplot(x=column, data=df, ax=axes[i])
        axes[i].set_title(f'Count Plot of {column}')
        axes[i].set_xlabel('Categories')
        axes[i].set_ylabel('Count')
        axes[i].tick_params(axis='x', rotation=45)

    # Hide unused subplots
    for j in range(num_columns, num_rows * 3):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()


def plot_categorical_features(df, target):
    # Determine the number of rows needed based on the number of columns
    num_columns = len(df.columns)
    num_rows = (num_columns + 2) // 3  # Add 2 to round up to the nearest multiple of 3

    # Create subplots
    fig, axes = plt.subplots(num_rows, 3, figsize=(15, 5*num_rows))
    axes = axes.flatten()

    # Plot each categorical variable
    for i, column in enumerate(df.columns):
        sns.boxplot(x=column, y=target, data=df, ax=axes[i])
        axes[i].set_title(f'Box Plot of {column} against {target}')
        axes[i].set_xlabel('Categories')
        axes[i].set_ylabel(target)
        axes[i].tick_params(axis='x', rotation=45)

    # Hide unused subplots
    for j in range(num_columns, num_rows * 3):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()

def cramers_v(x, y):
    confusion_matrix = pd.crosstab(x, y)
    chi2, _, _, _ = chi2_contingency(confusion_matrix)
    n = confusion_matrix.sum().sum()
    phi2 = chi2 / n
    r, k = confusion_matrix.shape
    phi2corr = max(0, phi2 - ((k-1)*(r-1))/(n-1))
    rcorr = r - ((r-1)**2)/(n-1)
    kcorr = k - ((k-1)**2)/(n-1)
    return np.sqrt(phi2corr / min((kcorr-1), (rcorr-1)))
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display
def check_data_quality(df, show_head=True, show_info=True, show_missing=True,  show_duplicates=True,show_value_counts = True):
    """
    Performs a comprehensive check on a DataFrame, including:
    - Data structure information
    - Missing values
    - Unique values
    - Duplicate rows
    - Categorical column distributions
    - Numeric column summary
    """
    # Show basic info
    if show_info:
        print("DataFrame Info:")
        df.info()

    # Show data types per column
    print('------------------------------------')
    print("\nUnique Data Types Per Column:")
    print(df.apply(lambda col: list(set(col.map(type)))))

    # Show the first 5 rows
    if show_head:
        print('------------------------------------')
        print("\nFirst 5 Rows:")
        display(df.head(5))

    # Show missing values summary
    if show_missing:
        print('------------------------------------')
        print("\nMissing Values Summary:")
        print(df.isnull().sum())


    # Show duplicate rows count
    if show_duplicates:
        print('------------------------------------')
        print("\nTotal Duplicate Rows:", df.duplicated().sum())

    # Show per-column duplicate value counts
    if show_value_counts:
        print('------------------------------------')
        print("\nPer-Column Duplicate Value Counts:")
        duplicate_counts = {col: (df[col].value_counts() > 1).sum() for col in df.columns}
        print(pd.Series(duplicate_counts).sort_values(ascending=False))
def plot_missing_percentage(df):
    """
    Plots the percentage of missing values for each column in a DataFrame.
    If there are no missing values, it prints a message instead of plotting.
    """
    df.replace(' ', np.nan, inplace=True)
    missing_percent = df.isnull().mean() * 100
    missing_percent = missing_percent[missing_percent > 0].sort_values()

    if missing_percent.empty:
        print("No missing values in the dataset.")
        return  # Exit function without plotting

    plt.figure(figsize=(12, 6))
    ax = missing_percent.plot(kind='barh', color='salmon')

    # Add value labels on the bars
    for index, value in enumerate(missing_percent):
        plt.text(value + 0.5, index, f"{value:.2f}%", va='center', fontsize=10)

    plt.xlabel("Percentage of Missing Values")
    plt.ylabel("Columns")
    plt.title("Missing Data Percentage by Column")
    plt.show()
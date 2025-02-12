import pandas as pd 
import numpy as np
import os
import matplotlib.pyplot as plt
from IPython.display import display
from pathlib import Path
import plotly.express as px
def save_to_csv(df, folder_name, file_name):
    """
    Save a DataFrame as a CSV file in a folder relative to the current directory,
    using pathlib.
    
    Parameters:
        df (pd.DataFrame): The DataFrame to be saved.
        folder_name (str): The target folder name.
        file_name (str): The CSV file name (e.g., "data.csv").
    
    Returns:
        str: The full path of the saved CSV file.
    """
    # Create a Path 
    folder_path = Path(folder_name)
    
    # Create the folder if it doesn't exist
    folder_path.mkdir(parents=True, exist_ok=True)
    print(f"Folder '{folder_name}' has been created or already exists.")
    
    # Construct the full file path
    file_path = folder_path / file_name
    
    # Save the DataFrame to a CSV file
    df.to_csv(file_path, index=False)
    print(f"File saved to: {file_path}")
    
    return 
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


def save_sunburst_charts(df,cols, output_folder="charts"):
    """
    Generates and saves a sunburst chart for each unique value in 'CATEGORY_1' of the given DataFrame.
    
    The function does the following:
      1. Selects the columns 'CATEGORY_1', 'CATEGORY_2', and 'CATEGORY_3'.
      2. Replaces any empty strings or whitespace-only strings with 'unknown'.
      3. Fills any NaN values with 'unknown'.
      4. Creates an output folder if it doesn't exist.
      5. For each unique CATEGORY_1, it filters the DataFrame and creates a sunburst chart.
      6. Saves each chart as an HTML file in the output folder.
    
    Parameters:
      df (pd.DataFrame): The input DataFrame containing at least the columns 'CATEGORY_1', 'CATEGORY_2', and 'CATEGORY_3'.
      output_folder (str): The folder where the charts will be saved (default is "charts").
    """
    # Select only the required columns

    
    # Replace empty strings (or strings containing only whitespace) with 'unknown'
    df = df.replace(r'^\s*$', 'unknown', regex=True)
    df.fillna('unknown', inplace=True)
    
    # Get unique values from CATEGORY_1
    unique_categories = df['CATEGORY_1'].unique()
    
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # For each unique CATEGORY_1, create and save a sunburst chart
    for cat in unique_categories:
        df_filtered = df[df['CATEGORY_1'] == cat]
        
        fig = px.sunburst(
            df_filtered,
            path=cols,
            title=f"Sunburst Chart for {cat}"
        )
        
        # Only show the labels in the chart
        fig.update_traces(textinfo='label')
        
        # Create a safe file name for the category
        safe_cat = "".join([c if c.isalnum() else "_" for c in str(cat)])
        file_name = os.path.join(output_folder, f"sunburst_{safe_cat}.html")
        
        # Save the chart as an HTML file
        fig.write_html(file_name)
        print(f"Chart for {cat} saved to {file_name}")
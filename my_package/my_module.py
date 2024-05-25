import pandas as pd

def clean_missing_values(df, strategy='mean'):
    """
    Clean missing values in a DataFrame.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame.
    strategy (str): The strategy to use for filling missing values. Options are 'mean', 'median', 'mode'.
    
    Returns:
    pd.DataFrame: The DataFrame with missing values filled.
    """
    if strategy == 'mean':
        return df.fillna(df.mean())
    elif strategy == 'median':
        return df.fillna(df.median())
    elif strategy == 'mode':
        return df.fillna(df.mode().iloc[0])
    else:
        raise ValueError("Strategy not recognized. Use 'mean', 'median', or 'mode'.")

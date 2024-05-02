import pandas as pd 

def lag_columns(df, lag_columns):
    # Create a copy of the DataFrame to avoid modifying the original
    lagged_df = df.copy()
    
    # Shift each specified column by one day and create new lagged columns
    for column in lag_columns:
        lagged_df[f'{column}_lag_1'] = df[column].shift(1)

    # Drop rows with NaN values resulting from the shift
    lagged_df.dropna(inplace=True)
    
    return lagged_df
    
# example-usage:
# lag_columns = ['taken_units', 'free_units', 'capacity_rate', 'availability']
# lagged_days = [1, 2, 3, 7]  
# df = lag_columns(df, lag_columns, lagged_days)

# add time features to the df
def extract_date_features(df, date_column):
    # convert date column to datetime
    df[date_column] = pd.to_datetime(df[date_column])
    df = df.sort_values(by=date_column)
    # extract year, month, day, and day of week
    df['year'] = df[date_column].dt.year
    df['month'] = df[date_column].dt.month
    df['day'] = df[date_column].dt.day
    df['day_of_week'] = df[date_column].dt.dayofweek + 1  # Monday = 1, Sunday = 7
    return df
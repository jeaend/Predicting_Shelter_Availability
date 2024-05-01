import pandas as pd 

# lags the specified columns 
def lag_columns(df, lag_columns, lagged_days):
    for column in lag_columns:
        for lag in lagged_days:
            # create a new column with the lagged values
            df[f'{column}_lag_{lag}'] = df[column].shift(lag)

    # drop rows with NaN values resulting from the shift
    df.dropna(inplace=True)
    
    return df 

# example-usage:
# lag_columns = ['taken_units', 'free_units', 'capacity_rate', 'availability']
# lagged_days = [1, 2, 3, 7]  
# df = lag_columns(df, lag_columns, lagged_days)

# add time features to the df
def extract_date_features(df, date_column):
    # convert date column to datetime
    df[date_column] = pd.to_datetime(df[date_column])
    df = df.sort_values(by=date_column, inplace=True)
    # extract year, month, day, and day of week
    df['year'] = df[date_column].dt.year
    df['month'] = df[date_column].dt.month
    df['day'] = df[date_column].dt.day
    df['day_of_week'] = df[date_column].dt.dayofweek + 1  # Monday = 1, Sunday = 7
    return df
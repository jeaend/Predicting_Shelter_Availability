import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# checks if two df have same values and structures
# use this to validate cleaner methods
def df_equality(df1, df2):
    return df1.eq(df2).sum().sum() == df1.shape[0] * df1.shape[1] == df2.shape[0] * df2.shape[1]

# checks if concatenating multiple df into one by row was succesfull 
def check_concatenation(df_list, concatenated_df):
    total_rows = sum(df.shape[0] for df in df_list)
    return total_rows == concatenated_df.shape[0]

# changes data of all formats to DD.MM.YY + changes to
def date_to_european_format(df, column):
    # convert type 
    df[column] = pd.to_datetime(df['date'], errors='coerce')
    # change format to european 
    df[column] = df[column].dt.strftime('%d-%m-%Y')
    return df[column]

# retrieves correct and relevant data from climate
def preprocess_climate_data(url):
    # retrieve selected columns
    keep_columns = ['LOCAL_DATE', 'MIN_TEMPERATURE', 'MEAN_TEMPERATURE', 'MAX_TEMPERATURE', 'TOTAL_PRECIPITATION', 'SNOW_ON_GROUND']
    climate_df = pd.read_csv(url, usecols=keep_columns)
    climate_df.rename(columns=lambda x: x.strip().replace(" ", "_").lower(), inplace=True)
    
    # fill snow_on_ground nan with 0
    climate_df['snow_on_ground'].fillna(0, inplace=True)

    # implicitly convert local_date to datetime format 
    climate_df['local_date'] = pd.to_datetime(climate_df['local_date'])
    climate_df.sort_values(by='local_date', inplace=True)
    climate_df['local_date'] = climate_df['local_date'].dt.strftime('%d.%m.%y')
    
    # sort by local_date, should be the case already -- making sure the rolling window works 
    climate_df.rename(columns={'local_date': 'date'}, inplace=True)

    climate_df.reset_index(drop=True, inplace=True)
    columns_with_nan = climate_df.columns[climate_df.isna().any()].tolist()

    # Fill NaN values in var_list using rolling mean with window size of 2 and min_periods=1
    climate_df[columns_with_nan] = climate_df[columns_with_nan].fillna(climate_df[columns_with_nan].rolling(window=2, min_periods=1).mean())

    return climate_df
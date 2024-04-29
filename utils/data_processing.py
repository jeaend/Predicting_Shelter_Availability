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

def fix_shelter_dates(df, column):
    pattern1 = '(\d{2})-(\d{2})-(\d{2})'
    pattern2 = '(\d{4})-(\d{2})-(\d{2})'
    df[column] = df['date'].astype(str)
    # Extract year, month, and day components using regex
    df[['year', 'month', 'day']] = df[column].str.extract(pattern1).fillna(df[column].str.extract(pattern2))
    # Convert extracted components to integers
    df[column] = df['day'].astype(str) + '.' + df['month'].astype(str) + '.' + df['year'].astype(str)
    df.drop(columns=['year', 'month', 'day'], inplace=True)
    return df

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
    climate_df.rename(columns={'local_date': 'date'}, inplace=True)

    
    # sort by local_date, should be the case already -- making sure the rolling window works 
    climate_df.rename(columns={'local_date': 'date'}, inplace=True)

    climate_df.reset_index(drop=True, inplace=True)
    columns_with_nan = climate_df.columns[climate_df.isna().any()].tolist()

    # Fill NaN values in var_list using rolling mean with window size of 2 and min_periods=1
    climate_df[columns_with_nan] = climate_df[columns_with_nan].fillna(climate_df[columns_with_nan].rolling(window=2, min_periods=1).mean())

    return climate_df


# retrieves correct and relevant data from shelter
def preprocess_shelter_data(urls):
    # read data from each URL into df
    dfs = [pd.read_csv(url, index_col=False) for url in urls]

    # concatenate all DataFrames into one
    shelter_df = pd.concat(dfs, ignore_index=True)
    
    # clean column names
    shelter_df.rename(columns=lambda x: x.strip().replace(" ", "_").lower(), inplace=True)
    shelter_df.rename(columns={'occupancy_date': 'date'}, inplace=True)

    shelter_df = fix_shelter_dates(shelter_df, 'date')

    # filter
    drop_values = ['Interim Housing', 'Alternative Space Protocol', 'Top Bunk Contingency Space', 'Isolation/Recovery Site']
    shelter_df = shelter_df[(shelter_df['program_model'] == 'Emergency') & 
                        (~shelter_df['overnight_service_type'].isin(drop_values))]

    # ill location_city NaN 
        # group by 'shelter_id' and get the first non-null value of 'location_city'
    shelter_id_mapping = shelter_df.groupby('shelter_id')['location_city'].first()
        # fill missing values in 'location_city' based on 'shelter_id'
    shelter_df['location_city'] = shelter_df.apply(lambda row: shelter_id_mapping.get(row['shelter_id'], row['location_city']), axis=1)
    shelter_df.loc[shelter_df['shelter_id'] == 27, 'location_city'] = 'Toronto'

    # clean values
    shelter_df['capacity_type'] = shelter_df['capacity_type'].map(lambda x: x.split(' ')[0] if isinstance(x, str) else x)
        # turn room and beds into general unit
    shelter_df['taken_units'] = shelter_df.apply(lambda row: row['occupied_rooms'] if row['capacity_type'] == 'Room' else row['occupied_beds'], axis=1)
    shelter_df['free_units'] = shelter_df.apply(lambda row: row['unoccupied_rooms'] if row['capacity_type'] == 'Room' else row['unoccupied_beds'], axis=1)
    shelter_df.drop(columns=['occupied_beds', 'unoccupied_beds', 'occupied_rooms', 'unoccupied_rooms'], inplace=True)
   
    # add columns 
    shelter_df['capacity_rate'] = shelter_df['taken_units'] / (shelter_df['taken_units'] + shelter_df['free_units'])
    shelter_df['availability'] = shelter_df['free_units'] / (shelter_df['taken_units'] + shelter_df['free_units'])

    columns_to_keep = ['date', 'location_city', 'sector', 'overnight_service_type', 'capacity_type', 'taken_units', 'free_units', 'capacity_rate', 'availability']
    
    return shelter_df[columns_to_keep]

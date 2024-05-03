# Shelter Capacity in Toronto

## Overview

This project aims to investigate the relationship between shelter occupancy rates and weather conditions in Toronto. By analyzing historical shelter occupancy data alongside weather data, the project seeks to answer the question: Is there a relationship between the occupancy rate and the weather? Understanding this relationship can provide valuable insights for resource allocation, policy-making, and intervention planning to address homelessness and ensure the well-being of vulnerable populations.

## Structure
```
data/
├── processed/              # Processed data files after cleaning  
│   ├── climate/            # Processed climate data files  
│   └── shelter/            # Processed shelter occupancy data files  
├── raw/                    # Raw data files  
│   ├── climate/            # Raw climate data files  
│   ├── deaths/             # Directory for raw death data
│   └── shelter/            # Raw shelter occupancy data files  
├── Data_Processing.md      # Documentation detailing data processing steps  

notebooks/                  # Jupyter notebooks for data cleaning and processing  
├── eda/                    # Exploratory Data Analysis notebooks
        aggregate_to_daily.ipynb                   # Notebook for aggregating data to daily level
        failed_time_series_model.ipynb             # Notebook for failed time series model
        feature_enrichment.ipynb                   # Notebook for enriching features
        model_on_aggregate.ipynb                   # Notebook for modeling on aggregated data
        shelter_climate_eda.ipynb                  # Notebook for EDA on shelter and climate data
        wrangling_cliamte_warming_shelter.ipynb    # Notebook for data wrangling on climate warming and shelter
├── preprocessing/         # Notebooks for data preprocessing
        climate_data_cleaning.ipynb                # Notebook for cleaning climate data
        shelter_data_cleaning.ipynb                # Notebook for cleaning shelter data
├── saving_data/            # Notebooks for saving data
        data_to_database.ipynb                      # Notebook for saving data to a database
        merged_data_to_csv.ipynb                    # Notebook for merging and saving data to CSV

utils/                  # Helper Functions
        data_from_db.py     # Script for extracting data from a database
        data_processing.py  # Script for data processing tasks
        eda.py              # Script for Exploratory Data Analysis tasks
        model_helper.py     # Script containing helper functions for modeling
        modeling.py         # Script for model development

README.md                   # Project README file providing an overview  
Shelter Capacity.key        # Keynotes file with presentation
```

## Installation

1. Clone this repository to your local machine.
2. If you wish to save the data to a db, make sure to have it setup. I used MySQLWorkbench and Mysql server. (notebooks/saving_data/data_to_database.ipynb)
- To install the required dependencies, including SQLAlchemy, you can use pip: pip install sqlalchemy
3. The Scripts are documented ans self explanatory 

## Usage

- Data: Raw and processed data files are stored in the data directory. Raw data is stored in the raw directory, while processed data is stored in the processed directory.
- Notebooks: Jupyter notebooks for exploratory data analysis (EDA) and preprocessing are located in the notebooks directory.
- Utils: Utility scripts and modules are stored in the utils directory.

## Data
**Please refer to [Data Processing](data/Data_Processing.md) for a comprehensive description of the data**

The shelter occupancy data was sourced from the City of Toronto's Open Data Portal. You can find the dataset here.

The climate data for Toronto City from January 1, 2021, to March 31, 2024, was obtained from the Climate Data Canada website. You can download the data for Toronto City from the Climate Data Canada website using the specified parameters.

This climate data will be used to analyze weather conditions and their impact on shelter occupancy rates.
## Methodology

The methodology involves data preprocessing, feature engineering, model selection, and evaluation.

## Results

The main findings from my project are as follows:

Unfortunately, despite my efforts, I was unable to establish a clear relationship between shelter occupancy rates and weather conditions. The high occupancy rates and persistent demand for shelters in Toronto make it challenging to identify such a correlation definitively.

However, my analysis did reveal that the city of Toronto takes action during periods of dangerously low temperatures, indicating a proactive approach to address weather-related risks for vulnerable populations. Nonetheless, whether these measures are adequate remains an open question.

Furthermore, my findings underscore the pressing need for change in addressing homelessness and ensuring the well-being of marginalized communities in Toronto.

You can find the graphs used in the presentation here: 
https://public.tableau.com/app/profile/jeanne.endres/viz/Shelter_17145561256700/snow_and_warming_centers?publish=yes

## Future Work

For future work, there are several avenues to explore:

- Consider analyzing time series data to capture trends and patterns over time.
- Experiment with different datasets or additional variables to see if they provide insights into the relationship between shelter occupancy and weather.
- Conduct further analysis by selecting different columns or features to uncover potential correlations or causations.

I'm eager to explore these avenues or any other areas of interest to continue advancing our understanding of homelessness and its intersection with weather conditions in Toronto.

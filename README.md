# Predicting Shelter Availability in Toronto

## Overview

This project aims to predict the availability of shelter beds in Toronto using a machine learning model trained on historical shelter occupancy data and weather conditions. With shelter occupancy rates often reaching 100%, predicting availability as a binary (Y/N) variable presents a practical challenge. By integrating features such as temperature, weather conditions, holidays, and other relevant factors, the model will address the imbalanced nature of the data and provide valuable insights for resource allocation and planning. Additionally, the project explores methods for generalizing the model to other districts, laying the groundwork for potential scalability and wider applicability. 

## Structure
```
data/
├── raw/                    # Raw data files  
│   ├── climate/            # Raw climate data files  
│   │   └── climate-toronto2021-Q1-2024.csv  
│   └── shelter/            # Raw shelter occupancy data files  
│       ├── daily-shelter-overnight-service-occupancy-capacity-2021.csv  
│       ├── daily-shelter-overnight-service-occupancy-capacity-2022.csv  
│       ├── daily-shelter-overnight-service-occupancy-capacity-2023.csv  
│       └── daily-shelter-overnight-service-occupancy-capacity-Q1:2024.csv  
├── processed/              # Processed data files after cleaning  
│   ├── climate/            # Processed climate data files  
│   └── shelter/            # Processed shelter occupancy data files  
├── Data_Processing.md      # Documentation detailing data processing steps  
└── notebooks/              # Jupyter notebooks for data cleaning and processing  
    ├── cleaning/           # Notebooks for cleaning raw data  
    │   ├── climate_data_cleaning.ipynb   # Jupyter notebook for cleaning climate data  
    │   └── shelter_data_cleaning.ipynb   # Jupyter notebook for cleaning shelter data  
    └── data_processing.ipynb             # Jupyter notebook for data preprocessing pipeline  

src/                        # Source code directory  
├── data_processing.py      # Python script for data preprocessing tasks  
├── modeling.py             # Python script for model development  
└── evaluation.py           # Python script for model evaluation  

README.md                   # Project README file providing an overview  
```

## Installation

[Instructions on how to install any dependencies required to run the project and how to set it up.]

## Usage

[Instructions on how to use the project, including any necessary commands and parameters.]

## Data
**Please refer to [Data Processing](data/DATA_PROCESSING.md) for a comprehensive description of the data and processing decisions made.**

The shelter occupancy data was sourced from the City of Toronto's Open Data Portal. You can find the dataset here.

The climate data for Toronto City from January 1, 2021, to March 31, 2024, was obtained from the Climate Data Canada website. You can download the data for Toronto City from the Climate Data Canada website using the specified parameters.

This climate data will be used to analyze weather conditions and their impact on shelter occupancy rates.
## Methodology

The methodology involves data preprocessing, feature engineering, model selection, and evaluation. Techniques such as oversampling, undersampling, or using algorithms designed to handle imbalanced data are applied. Model performance is assessed using metrics like precision, recall, F1-score, or area under the ROC curve (AUC-ROC).

## Results

[Summary of the main findings and results obtained from the project.]

## Future Work

Ideas for future improvements or extensions to the project, such as exploring additional features, refining model architecture, or incorporating real-time data.

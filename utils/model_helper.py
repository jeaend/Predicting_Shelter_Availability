from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd


# preprocess data, one hot encode categoricals, target is numericall, no scaling on numerical
def preprocess_data(X, y, test_size=0.2, random_state=42):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    # separate numerical and categorical columns
    numerical_columns = X.select_dtypes(include=['float64', 'int64']).columns
    categorical_columns = X.select_dtypes(object).columns

    # extract numerical and categorical data
    X_train_numerical = X_train[numerical_columns]
    X_train_categorical = X_train[categorical_columns]

    X_test_numerical = X_test[numerical_columns]
    X_test_categorical = X_test[categorical_columns]

    # one-hot encode categorical data
    encoder = OneHotEncoder(sparse_output=False, drop='first')
    X_train_categorical.columns = [str(col) for col in X_train_categorical.columns]
    X_test_categorical.columns = [str(col) for col in X_test_categorical.columns]

    encoded_data = encoder.fit_transform(X_train_categorical)
    X_train_cat_hot = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(X_train_categorical.columns))

    encoded_test_data = encoder.transform(X_test_categorical)
    X_test_cat_hot = pd.DataFrame(encoded_test_data, columns=encoder.get_feature_names_out(X_train_categorical.columns))

    # reset index for numerical data
    X_train_numerical.reset_index(drop=True, inplace=True)
    X_test_numerical.reset_index(drop=True, inplace=True)

    # concatenate numerical and encoded categorical data
    X_train = pd.concat([X_train_cat_hot, X_train_numerical], axis=1)
    X_test = pd.concat([X_test_cat_hot, X_test_numerical], axis=1)

    return X_train, X_test, y_train, y_test




# takes train and test data and compares different models 
def build_regression_models(X_train, X_test, y_train, y_test):
    models = {
        'Linear Regression': LinearRegression(),
        'Random Forest': RandomForestRegressor(random_state=42),
        'Gradient Boosting': GradientBoostingRegressor(random_state=42)
    }
    
    results = {'Model': [], 'Mean Squared Error': [], 'R-squared': []}
    
    # fit models and calculate scores
    for model_name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        results['Model'].append(model_name)
        results['Mean Squared Error'].append(mse)
        results['R-squared'].append(r2)
    
    # convert results to DataFrame
    results_df = pd.DataFrame(results)
    
    return results_df

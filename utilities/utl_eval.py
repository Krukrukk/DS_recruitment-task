import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def preperation_data(data: pd.DataFrame, params: dict):
    """
    Function to split data into training and test set based on test set breakdown and seed.
        """
    X_data = data.drop(['y'], axis=1).ffill()
    y_data = data['y'].values
    X_train, X_test, y_train, y_test = train_test_split(X_data,
                                                        y_data,
                                                        test_size=float(params['num_of_test_samples']/len(X_data)),
                                                        random_state=params['seed']
                                                        )
    dataset = {
        "train":{
            "X": X_train,
            "y": y_train
        },
        "test":{
            "X": X_test,
            "y": y_test
        }
    }
    return dataset


def eval_metrics(true: list, pred):
    """
    Function to test the quality of regression models.
    Parameters:
        true: list <- truthful data
        pred: list <- predicted data
    Return:
        rmse: float <- root mean square error
        mae: float <- mean absolute error
        r2: float <- coefficient of determination
    """
    rmse = np.sqrt(mean_squared_error(true, pred))
    mae = mean_absolute_error(true, pred)
    r2 = r2_score(true, pred)
    return rmse, mae, r2
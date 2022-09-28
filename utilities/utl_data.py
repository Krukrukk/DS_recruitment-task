import pandas as pd


def check_inactive(y: list, inactive_val: int = 10000):
    """
    Function to detect sensor inactivity.
    Parameters:
        y: list                 <- signal
        inactive_val: int=10000 <- value indicating that the device is inactive
    Return:
        output: list      <- list of all inactive compartments
    """
    all_interval = []
    interval = []
    idx = 0
    while idx < len(y) - 1:
        if y[idx] == y[idx + 1] and inactive_val == y[idx]:
            if (len(interval) == 0):
                interval.append(idx)
            idx += 1
        else:
            if (len(interval) > 0):
                interval.append(idx)
                all_interval.append(interval)
            interval = []
            idx += 1
    return all_interval


def filling_data(data_main: pd.DataFrame, data_time: pd.DataFrame):
    """
    Function to fill in missing values.
    Parameters:
        data_main: pd.DataFrame <- main dataframe
        data_time: pd.DataFrame <- dataframe with date
    Return:
        output: pd.DataFrame    <- main dataframe with completed missing values
    """
    data_time['DATE'] = pd.to_datetime(data_time['DATE'], format='%Y-%m-%d')
    data_main.index = data_time['DATE']
    data_main = data_main.ffill(axis=0)
    data_main = data_main.bfill(axis=0)
    return data_main

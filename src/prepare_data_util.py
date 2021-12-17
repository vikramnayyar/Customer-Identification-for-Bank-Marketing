"""

The script declare the functions used in prepare_data.py 

"""
import pathlib
import pandas as pd
from logzero import logger, logfile
import numpy as np
import scipy
import scipy.stats as stats

from utility import create_log, parse_config, read_data


# Converting columns to categorical variables 
def convert_cat(df, col_list): 
    df_temp = pd.DataFrame() 
    df_temp = df
    col_list = col_list
    
    for col in col_list:
        df_temp[col] = df_temp[col].astype('category')
        df_temp[col] = df_temp[col].cat.codes
    
    logger.info('Categorical conversion of columns was completed successfully.')  # Writing to logfile
    return df_temp



def cols_with_ouliers(df):
    def outlier_cols(x):    
        n = len(x)
        mean_x = np.mean(x)
        sd_x = np.std(x)
        numerator = max(abs(x-mean_x))
        g_calculated = numerator/sd_x
        t_value = stats.t.ppf(1 - 0.05 / (2 * n), n - 2)
        g_critical = ((n - 1) * np.sqrt(np.square(t_value))) / (np.sqrt(n) * np.sqrt(n - 2 + np.square(t_value)))
        return col if (g_critical) < g_calculated else 0
    
    # Finding columns with outliers
    col_with_outliers = []
    for col in df.columns:
        outlier_col = outlier_cols(df[col])
        col_with_outliers.append(outlier_col)
    
    while (col_with_outliers.count(0)):
        col_with_outliers.remove(0)
    
    logger.info('Columns with outliers are: {}'.format(col_with_outliers) )
    return col_with_outliers



def grubbs_test(x):
    n = len(x)
    mean_x = np.mean(x)
    sd_x = np.std(x)
    numerator = max(abs(x-mean_x))
    g_calculated = numerator/sd_x
    print("Grubbs Calculated Value:",g_calculated)
    t_value = stats.t.ppf(1 - 0.05 / (2 * n), n - 2)
    g_critical = ((n - 1) * np.sqrt(np.square(t_value))) / (np.sqrt(n) * np.sqrt(n - 2 + np.square(t_value)))
    print("Grubbs Critical Value:",g_critical)
    if g_critical > g_calculated:
        logger.info("From grubbs_test we observe that calculated value is lesser than critical value, Accept null hypothesis and conclude that there is no outlier\n")
    else:
        logger.info("From grubbs_test we observe that calculated value is greater than critical value, Reject null hypothesis and conclude that there is an outliers\n")
        

def scaling_outliers(df, cols_with_outliers):
    for col in cols_with_outliers:
        if col != 'pdays' and col != 'balance':    # pdays and balance have negative values, so scaling will result in NaNs
            df[col] = (df[col]**(1/3.7))
    return df
        

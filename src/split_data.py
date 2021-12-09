"""

The script obtains correlation heatmap 
& executes train-test splitting 

"""

import pathlib
import pandas as pd
from logzero import logger, logfile

from utility import create_log, parse_config, read_data
from split_data_util import analyze_corr, train_test_split

create_log("split_data.log")  # Creating log file

##################################################
#-----------------Reading Dataset-----------------
##################################################

config_path = "../config/config.yaml"   
config = parse_config(config_path)   # read config file
data_path = config["split_data"]["data"]   # read dataset
df_clean = read_data(data_path)


#######################################
#---------Analyzing Correlation--------
#######################################

analyze_corr(df_clean, "deposit")


#######################################
#---------- Train-Test Split ----------
#######################################

train_test_split(df_clean, "deposit", "deposit")   # col_1 is for label and col_2 is for stratification
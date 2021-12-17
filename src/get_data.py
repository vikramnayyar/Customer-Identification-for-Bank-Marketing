"""

The script reads and analyzes the dataset. After cleaning, it is oberved that
dataset cleaning is not required.

Also, the **locations** and **restaurant type** dictionaries are saved. This is 
required for the application to accept user inputs. 

"""

import pandas as pd
from logzero import logger, logfile
import pickle
from utility import create_log, parse_config, read_data
from get_data_util import analyze_data, extract_dict

create_log("get_data.log")  # Creating log file


##################################################
#-------------------Reading Data------------------
##################################################

config_path = "../config/config.yaml"   
config = parse_config(config_path)   # read config file
data_path = config["get_data"]["data"]   # read dataset
df = read_data(data_path)
        
analyze_data(df)   # Analyzing dataset

# This dataset deos not require any cleaning

# Saving data
df.to_csv('../data/clean_data.csv', index = False)    # Saving the file in the path

logger.info("Cleaned dataset was saved successfully.")

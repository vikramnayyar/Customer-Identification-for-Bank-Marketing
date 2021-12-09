"""

The script obtains various visualizations of the cleaned dataset 
& stores them in "visualization" directory

"""
import os
import pathlib
import pandas as pd

from utility import create_log, parse_config, read_data
from data_analysis_util import dataset_balance, box_plot, grouped_bar_plot

create_log("data_analysis.log")  # Creating log file

##################################################
#-----------------Reading Dataset-----------------
##################################################

config_path = "../config/config.yaml"   
config = parse_config(config_path)   # read config file
data_path = config["data_analysis"]["data"]   # read dataset
df_clean = read_data(data_path)

# df_clean['rate'] = pd.to_numeric(df_clean['rate'], downcast = 'float') # Converting ratings to float

os.chdir('../visualizations')  # directory to save visualization figures


# #################################################
# ---------------- Dataset Balance ----------------
# #################################################

dataset_balance(df_clean, "balance")


# #################################################
# --------- 1. Balance Type vs Rating -------------
# #################################################

box_plot(df_clean, "balance", "bal_vs_deposit")


##################################################
#------------- 2. Age vs Deposit -----------------
##################################################

box_plot(df_clean, "age", "age_vs_deposit")


##################################################
#------------- 3. Job vs Deposit -----------------
##################################################

grouped_bar_plot(df_clean, "job", "job_vs_deposit")


##################################################
#------------- 4. Marital vs Deposit -------------
##################################################

grouped_bar_plot(df_clean, "marital", "marital_vs_deposit")


##################################################
#------------- 5. Education vs Deposit -----------
##################################################

grouped_bar_plot(df_clean, "education", "education_vs_deposit")


os.chdir('../src')  # resetting to src path 
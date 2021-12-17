"""

The declares common functions used by multiple scripts

"""

import os
import pathlib
from pathlib import Path

import requests
import pandas as pd
import yaml

from logzero import logger, logfile

####################################
#--------Reading Config File--------
####################################

def parse_config(config_path):
    with open(config_path, "rb") as f:
        config = yaml.safe_load(f)
    return config

####################################
#---------Creating Log File---------
####################################

def create_log(log_name):
    tgt_path = pathlib.Path.cwd().parent.joinpath('log')
    logfile(tgt_path/log_name)     # Creating logfile


####################################
#---------Download Dataset----------
####################################

def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                
def download_dataset():
    file_id = config["get_data"]["download_id"]   # read dataset download id
    destination = pathlib.Path.cwd().parent.joinpath('data/restnt_data.csv')
    download_file_from_google_drive(file_id, destination)
    logger.info('Dataset was successfully downloaded')


####################################
#-------------Read Data-------------
####################################

def read_data(data_path):

    try:
        df = pd.read_csv(data_path)
        logger.info('Dataset with {} and {} features was loaded successfully.'.format(*df.shape))  # Writing to logfile
        return df
    
    except:
        logger.error('Dataset was not loaded. Please ensure that dataset is provided and is named correctly.')
    

####################################
#-----------Analyze Data------------
####################################

def analyze_data(df): 
    logger.info('\n * Size of dataframe: {}\n'.format(df.shape))
    logger.info('* Datatype of columns are:')
    logger.info('{}\n\n'.format(df.info()))
    logger.info('* Column-wise NaNs can be identified as: ')
    logger.info('{}\n'.format(df.isnull().sum()))
    logger.info('Total NaNs:{}'.format(df.isnull().sum().sum()))

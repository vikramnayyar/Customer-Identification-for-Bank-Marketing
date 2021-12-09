"""

The script declare the functions used in get_data.py 

"""

import pandas as pd
from logzero import logger, logfile


# def download_dataset():
#     file_id = config["get_data"]["download_id"]   # read dataset download id
#     destination = pathlib.Path.cwd().parent.joinpath('data/restnt_data.csv')
#     download_file_from_google_drive(file_id, destination)
#     logger.info('Dataset was successfully downloaded')



def analyze_data(df): 
    logger.info('\n * Size of dataframe: {}\n'.format(df.shape))
    logger.info('* Datatype of columns are:')
    logger.info('{}\n\n'.format(df.info()))
    logger.info('* Column-wise NaNs can be identified as: ')
    logger.info('{}\n'.format(df.isnull().sum()))
    logger.info('Total NaNs:{}'.format(df.isnull().sum().sum()))



def extract_dict(df, col):
    feature = df[col].astype('category')
    dict_val = dict(enumerate(feature.cat.categories))
    dict_inv = {a:b for b,a in dict_val.items()}
    
    return dict_inv



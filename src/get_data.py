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

# logger.info("Downloading dataset")
# # download_dataset()    # downloads data from gdrive (File size is larger than git limit)
# logger.info("Dataset downloaded successfully")


##################################################
#-------------------Reading Data------------------
##################################################

config_path = "../config/config.yaml"   
config = parse_config(config_path)   # read config file
data_path = config["get_data"]["data"]   # read dataset
df = read_data(data_path)
        
analyze_data(df)   # Analyzing dataset


##################################################
#-----------------Cleaning Dataset----------------
##################################################

# # renaming columns
# df.rename(columns = {'approx_cost(for two people)': 'approx_cost', 
#                      'listed_in(type)': 'type',	
#                      'listed_in(city)': 'city'}, inplace = True) 

# # removing unnecessary columns
# df = df.drop(['name', 'address', 'url', 'phone', 
#               'reviews_list', 'menu_item', 'dish_liked'], axis = 1)   # dish_liked and 'name' added additionally

# # Removing NaNs
# df.rate = df.rate.fillna('NEW')   # rate column

# df.rest_type = df.rest_type.fillna('Unknown')  # rest_type column

# # df.dish_liked = df.dish_liked.fillna('Unknown')  # dish_liked column

# df.cuisines = df.cuisines.fillna('Unknown')  # cuisines column

# df = df.dropna()   # location Column

# df.reset_index(drop=True, inplace=True)  # resetting indices

# logger.info('NaN removal can be verified:\n{}'.format(df.isnull().sum()))


# # Cleaning cost column
# df.approx_cost = df['approx_cost'].astype('str')
# df['approx_cost'] = df['approx_cost'].str.replace(',', '').str.replace(' ', '')
# df.approx_cost = df.approx_cost.astype('int')


# # Cleaning rate column
# df['rate'].astype('str')
# df['rate'] = df['rate'].str.replace('/5', '').str.replace(' ', '').str.replace('NEW', '-')
# df_clean = df[df['rate'] != '-'].copy()  # Removing rows without rating
# df_clean = df_clean.reset_index(drop=True)  # resetting indices


# Saving cleaned data
df.to_csv('../data/clean_data.csv', index = False)    # Saving the file in the path

logger.info("Cleaned dataset was saved successfully.")


# ###############################################
# #------------Saving Location Dictionary--------
# ###############################################

# location_dict = extract_dict(df_clean, 'location')

# file = open('../dict/locations_dict.pkl', 'wb')   # Open a file to store model
# pickle.dump(location_dict, file)   # dumping information to the file
# file.close()

# logger.info("The locations dictionary was saved successfully.")



# ###############################################
# #-----------Saving Rest-Type Dictionary--------
# ###############################################

# rest_type_dict = extract_dict(df_clean, 'rest_type')

# file = open('../dict/rest_type_dict.pkl', 'wb')   # Open a file to store model
# pickle.dump(rest_type_dict, file)   # dumping information to the file
# file.close()

# logger.info("The restaurant type dictionary was saved successfully.")
"""

The script converts the columns to categorical features 
& removes the outliers

"""

from utility import create_log, parse_config, read_data
from prepare_data_util import convert_cat, cols_with_ouliers, grubbs_test, scaling_outliers

create_log("prepare_data.log")  # Creating log file

##################################################
#-----------------Reading Dataset-----------------
##################################################
config_path = "../config/config.yaml"   
config = parse_config(config_path)   # read config file
data_path = config["prepare_data"]["data"]   # read dataset
df_clean = read_data(data_path)


################################################
#----------- Categorical Coversion--------------
################################################

col_list = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'month', 'poutcome', 'deposit', 'contact']
# col_list = ['online_order', 'book_table', 'location', 'rest_type', 'type', 'city']  # Columns requiring categorical conversion
df_clean = convert_cat(df_clean, col_list)  # converting to categories


################################################
#----------------Outlier Removal----------------
################################################
# Finding columns with outliers
cols_with_outliers = cols_with_ouliers(df_clean) 


for col in cols_with_outliers:
    if col != 'pdays' and col != 'balance':    # pdays and balance have negative values, so scaling will result in NaNs
        df_clean[col] = (df_clean[col]**(1/3.7))


# Columns that still have outliers
cols_with_outliers = cols_with_ouliers(df_clean) 


# Removing scaling transform from columns that still have outliers
for col in cols_with_outliers:
    if col != 'pdays' and col != 'balance':
        df_clean[col] = (df_clean[col]**(3.7))  


# Individually Removing Outliers from Columns

# Balance column
cut_off = 11000
for i in df_clean['balance']:
    if i >= cut_off:
        df_clean['balance'] = df_clean['balance'].replace(i, cut_off)
grubbs_test(df_clean['balance'])


# campaign column
cut_off = 12
for i in df_clean['campaign']:
    if i >= cut_off:
        df_clean['campaign'] = df_clean['campaign'].replace(i, cut_off)
grubbs_test(df_clean['campaign'])


# previous column
cut_off = 8
for i in df_clean['previous']:
    if i >= cut_off:
        df_clean['previous'] = df_clean['previous'].replace(i, cut_off)
grubbs_test(df_clean['previous'])


# pdays column
cut_off = 500
for i in df_clean['pdays']:
    if i >= cut_off:
        df_clean['pdays'] = df_clean['pdays'].replace(i, cut_off)

grubbs_test(df_clean['pdays'])


df_clean.to_csv("../data/prepared_data.csv", index = False)   # Saving file

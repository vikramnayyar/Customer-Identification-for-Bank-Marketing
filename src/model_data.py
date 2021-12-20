"""

The script models the split data using several classification models,
then; selects, optimizes and saves the best model 

"""
#import pandas as pd
from logzero import logger, logfile
import pickle

from model_data_util import compare_models, plot_feature_importance, optimize_best_model
from utility import create_log, parse_config, read_data

create_log("model_data.log")  # Creating log file

##################################################
#-------------Reading Dataset & Config------------
##################################################
config_path = "../config/config.yaml"   
config = parse_config(config_path)   # read config file

train_data = read_data(config["model_data"]["train_set"])
train_labels = read_data(config["model_data"]["train_labels"])
test_data = read_data(config["model_data"]["test_set"])
test_labels = read_data(config["model_data"]["test_labels"])
#n_estimators  = config["model_data"]["n_estimators"]


##################################################
#----------------Models Comparison----------------
##################################################
model_comparison = compare_models(train_data, train_labels, test_data, test_labels)

logger.info(model_comparison.head(10))
best_model = model_comparison.iloc[0][0]


###################################################
##--------Best Model Performance Optimization------
###################################################

plot_feature_importance(train_data, train_labels, best_model)

best_model, accuracy = optimize_best_model(train_data, train_labels, test_data, test_labels)

logger.info("Accuracy of the best model after optimization is {}".format(accuracy))
    

# Saving Model
file = open('../model/model.pkl', 'wb')   # Open a file to store model
pickle.dump(best_model, file)   # dumping information to the file
file.close()

"""

The script declares the functions used in 'model_data.py'

"""
import pandas as pd
from logzero import logger, logfile
import os

import numpy as np


from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.ensemble import ExtraTreesClassifier  
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from catboost import CatBoostClassifier

#import xgboost as xgb
from xgboost import XGBClassifier

#import lightgbm as lgb
from lightgbm import LGBMClassifier


import matplotlib.pyplot as plt
import seaborn as sns

from utility import parse_config


##################################################
#-----------------Reading Config------------------
##################################################

config_path = "../config/config.yaml"   
config = parse_config(config_path)   # read config file

##################################################
#-----------------Declaring Functions-------------
##################################################


def custom_cmap():
    import matplotlib.colors
    
    norm = matplotlib.colors.Normalize(-1,1)
    colors = [[norm(-1.0), "#e9fcdc"], 
              [norm(-0.6), "#d9f0c9"], 
              [norm( 0.6), "#4CBB17"],
              [norm( 1.0), "#0B6623"]]
    
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)
    return cmap



def plot_cm(model, cm, accuracy):

    fig = plt.figure(figsize=(7, 5))
    plt.title(model, size = 15)
     
    # Declaring heatmap labels
    group_counts = ['{0:0.0f}'.format(value) for value in cm.flatten()]
    group_percentages = ['{0:.2%}'.format(value) for value in cm.flatten()/np.sum(cm)]
    
    labels = [f"{v2}\n{v3}" for v2, v3 in zip(group_counts, group_percentages)]
    labels = np.asarray(labels).reshape(2,2)
    
    # Plotting heatmap 
    cmap = custom_cmap()
    sns.heatmap(cm, annot=labels, annot_kws={"size": 15}, fmt = '', cmap=cmap)
        
    # Adding figure labels
    plt.ylabel('Actual Values')
    plt.xlabel('Predicted Values \n \n Accuracy: {}'.format(round(accuracy, 4)))
    
    os.chdir('../visualizations')
    plt.savefig('cm_{}'.format(model))   # save figure
    os.chdir('../src')



def evaluate_model(model, test_data, test_labels, model_label):
    
    pred = model.predict(test_data)
    accuracy = accuracy_score(test_labels, pred)
    cm = confusion_matrix(test_labels, pred)
    
    if accuracy > 0.84:    
        plot_cm(model_label, cm, accuracy)
    return accuracy


def compare_models(train_data, train_labels, test_data, test_labels):
    
    model_comparison = pd.DataFrame()
    model_names = [ExtraTreesClassifier, AdaBoostClassifier, BaggingClassifier, 
                   GradientBoostingClassifier, RandomForestClassifier, DecisionTreeClassifier,
                   XGBClassifier, CatBoostClassifier, LGBMClassifier]
    
    
    model_labels = ["etc", "abc", "bc", "gbc", "rfc", "dtc", "xgb", "cbc", "lgbm"]
    i = 0
    
    for model_name in model_names:
        
        model_label = model_labels[i]
        i += 1   
        model = model_name()   # learning_rate does not work here
        model.fit(train_data, train_labels)
                
        accuracy = evaluate_model(model, test_data, test_labels, model_label)

        model_comparison = model_comparison.append({'model_name': model_name, 
                                                    'Accuracy': accuracy}, ignore_index = True)
    
    model_comparison.sort_values(by = ['Accuracy'], ascending = False, inplace = True ) 
    
    model_comparison.reset_index(drop = True)
    return model_comparison    


def plot_feature_importance(train_data, train_labels, best_model):

    best_model = best_model()
    best_model.fit(train_data, train_labels) 
    
    feature_importance = pd.DataFrame(best_model.feature_importances_,
                                   index = train_data.columns,
                                   columns=['importance']).sort_values('importance',ascending=False)
    
    # Plotting feature importance
    plt.figure(figsize=(20,8))
    plt.plot(feature_importance)
    plt.scatter(y=feature_importance.importance,x=feature_importance.index)
    plt.title(config["model_data"]["feature_importance"]["title"], fontsize = 16)
    plt.ylabel(config["model_data"]["feature_importance"]["ylabel"], fontsize=14)
    plt.xlabel(config["model_data"]["feature_importance"]["ylabel"], fontsize = 14)
    plt.grid()
    
    os.chdir("../visualizations")
    plt.savefig("feature_importance.png")
    os.chdir("../src")
    
    
def optimize_best_model(train_data, train_labels, test_data, test_labels):

    # Assigning categorical features
    cbc_params = {'loss_function': config["model_data"]["cbc_params"]["loss_function"], 
                  'eval_metric': config["model_data"]["cbc_params"]["loss_function"],
                  'cat_features': config["model_data"]["cbc_params"]["cat_features"],
                  'verbose': config["model_data"]["cbc_params"]["verbose"],
                  'random_seed': config["model_data"]["cbc_params"]["random_seed"],
                  'iterations': config["model_data"]["cbc_params"]["iterations"],
                  'max_depth': config["model_data"]["cbc_params"]["max_depth"]
                  }    


    # Declaring model
    model = CatBoostClassifier(**cbc_params)
    
    # Fitting model to train set 
    model.fit(train_data, train_labels,
              eval_set=(test_data, test_labels),
              use_best_model=True,
              plot=True
             );
                  
    model_label = "optimized_cbc"         
    accuracy = evaluate_model(model, test_data, test_labels, model_label)
    return model, accuracy    

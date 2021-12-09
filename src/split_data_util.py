"""

The script declares the functions used in 'split_data.py'

"""

import pathlib
import pandas as pd
from logzero import logger, logfile

import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import sklearn
from sklearn.model_selection import StratifiedShuffleSplit



def analyze_corr(df, col):
    # fig
    fig = plt.figure(figsize=(12, 12))
    
    # mask
    mask = np.triu(df.corr())
    
    # axes 
    axes = fig.add_axes([0, 0, 1, 1])
    sns.heatmap(df.dropna().corr(), annot=True, mask=mask, square=True, fmt='.2g',
                vmin=-1, vmax=1, center= 0, cmap='viridis', linecolor='white', 
                cbar_kws= {'orientation': 'vertical'}, ax=axes) 
    
    # title
    axes.text(-1, -1.5, 'Correlation', color='black', fontsize=24, fontweight='bold')
    
    plt.savefig('../visualizations/correlation_heatmap.png')
    
    # Printing correlations
    corr_matrix = df.corr()
    logger.info("The correlation of 'rating' with other columns is: {}".format(corr_matrix[col].sort_values()))



def train_test_split(df, col_1, col_2):
    
    df= df.reset_index(drop=True)
    
    # Identifying indices 
    split = StratifiedShuffleSplit(n_splits = 1, test_size = 0.2, random_state = 65)
    for train_index, test_index in split.split(df, df[col_2]):
        train_set = df.loc[train_index]
        test_set = df.loc[test_index]
          
    logger.info(f"\nRows in train set : {len(train_set)}\nRows in test set: {len(test_set)}\n\n")
    
    # train_set
    train_labels = train_set[col_1].copy()    # Storing feature in labels variable
    train_set = train_set.drop([col_1], axis = 1)       # removing train labels
    
    # test_set
    test_labels = test_set[col_1].copy()     # Storing feature in labels variable
    test_set = test_set.drop([col_1], axis = 1)   # removing labels from test set
    
    # Saving train and test sets 
    tgt_path = pathlib.Path.cwd().parent.joinpath('data/train_labels.csv')  # declaring file path
    train_labels.to_csv(tgt_path, index = False)   # saving file
    
    tgt_path = pathlib.Path.cwd().parent.joinpath('data/train_set.csv')  # declaring file path
    train_set.to_csv(tgt_path, index = False)   # saving file
    
    tgt_path = pathlib.Path.cwd().parent.joinpath('data/test_labels.csv')  # declaring file path
    test_labels.to_csv(tgt_path, index = False)   # saving file
    
    tgt_path = pathlib.Path.cwd().parent.joinpath('data/test_set.csv')  # declaring file path
    test_set.to_csv(tgt_path, index = False)   # saving file
    
    logger.info(f"\nRows in train data : {len(train_set)}\nRows in train labels: {len(train_labels)}\nRows in test data: {len(test_set)}\nRows in test labels: {len(test_labels)}\n")
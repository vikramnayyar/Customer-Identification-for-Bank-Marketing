"""

The script declares functions used in 'data_analysis.py'

"""

import os

import yaml
from logzero import logger

import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Patch
import plotly.graph_objects as go

from utility import parse_config

config_path = "../config/config.yaml"   
config = parse_config(config_path)   # read config file


def dataset_balance(df_clean, col):
    fig, ax = plt.subplots()
    sns.countplot(x = col, data = df_clean, palette = 'viridis')
    
    plt.title('Deposit Distribution of Bank Customers', fontsize = 16)
    plt.xlabel('Deposit', fontsize = 14)
    plt.ylabel('Total Customers', fontsize = 14)
    plt.xticks(fontsize = 12)
    plt.savefig("dataset_balance.png")

def box_plot(df_clean, col, plot_type):
    
    fig, ax = plt.subplots(1, 2, figsize=(15, 5))
    fig.suptitle(config["data_analysis"][plot_type]["title"], size = 18, y=1.08)
    
    # Subplot 1
    ax[0].hist(df_clean[df_clean["deposit"]=='no'][col], bins=30, alpha=0.5, color="green", label="Non-Depositors")
    ax[0].hist(df_clean[df_clean["deposit"]=='yes'][col], bins=30, alpha=0.5, color="blue", label="Depositors")
    
    ax[0].set_xlabel(config["data_analysis"][plot_type]["xlabel"], size = 14)
    ax[0].set_ylabel(config["data_analysis"][plot_type]["ylabel"], size = 14)
    ax[0].legend(fontsize = 11);
    
    # Subplot 2
    sns.boxplot(x=col, y="deposit", data=df_clean, orient="h", palette={ 'no':"#80e880", 'yes':"#2626ff"}, ax = ax[1])
    ax[1].get_yaxis().set_visible(False)
    ax[1].set_xlabel(config["data_analysis"][plot_type]["xlabel"], size = 14)
    
    color_patches = [
        Patch(facecolor="#80e880", label="Non-Depositors"),
        Patch(facecolor="#2626ff", label="Depositors")
    ]
    ax[1].legend(handles=color_patches, fontsize=11);
  
    plt.savefig(plot_type)  # saving figure
    

def grouped_bar_plot(df_clean, col, plot_type):
    
    fig, ax = plt.subplots()

    sns.catplot(col, hue = 'deposit', data=df_clean, kind="count", palette={'no':"#80e880", 'yes':"#2626ff"}, legend = False)
    
    color_patches = [
        Patch(facecolor="#80e880", label="Non-Depositors"),
        Patch(facecolor="#2626ff", label="Depositors")
    ]
    
    plt.title(config["data_analysis"][plot_type]["title"], size = 18, y=1.08) 
    plt.xlabel(config["data_analysis"][plot_type]["xlabel"], size = 14)
    plt.ylabel(config["data_analysis"][plot_type]["ylabel"], size = 14)
    plt.xticks(size = 12, rotation = 'vertical')
    plt.legend(handles = color_patches, fontsize = 12,  bbox_to_anchor=(1.4,1.05))
    
    plt.savefig(plot_type)  # saving figure
    plt.close(1) 
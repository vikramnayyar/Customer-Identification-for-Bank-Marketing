# Customer Identification for Bank Marketing Campaign

## Demo
The application is deployed in Heroku. The app is available in the link https://predict-bank-marketing.herokuapp.com/

## Introduction
An app is developed for bank marketing campaigns; that target customers interested in making term deposits. App is based on 16 inputs that predict whether a customer will deposit or not? The app was trained using <b>sklearn</b> models and is developed in <b>Streamlit</b>. 

## Dataset
The dataset consists of actual information obtained from a marketing campaign of a Portuguese banking institution. The bank launched this campaign to increase the term deposits. Often; each customer was contacted more than once, to determine as a depositor or non-depositor.

The dataset was acquired from UCI (University of California, Irvine) repository. It is avalailable in link: https://archive.ics.uci.edu/ml/datasets/bank+marketing). The dataset consists of <b>11162</b> rows and <b>15</b> features.    

## Problem Statement
Marketing a product or a service is very challenging. Identifying the right customer is vital for the marketing team. This can significantly reduce the resources and time. Furthermore, this allows the team to position the product correctly. Unfortunately, finding the right customer can be exhaustive and complicated. There are many features to consider and huge data to analyze. Thus conventionally; the marketing team relies on experience of the marketing experts and feedback of team. 

Due to vast facts originating from so many features; a mistake in identification of customer is inevitable. Missing a customer segment results as a loss to the institution. On contrary, identifying wrong segment of customers will result in wastage of resources and time (As faults in strategy is confirmed at a later stage). 

Therefore, such a project is vital for product marketing. 

## Goal
This work was performed as a personal project. The motivation was to obtain analysis of bank marketing campaign and identify customers that will make term deposits. For highest possible term deposits, a high accuracy was desirable for customer classification.   

An app classifying depositing customers, provides a very straightforward and intuitive means for identifying customers. This saves substantial <b>resources</b> and <b>time</b>. Also, this apporach is easily reproducible, thus; provides a <b>common</b> marketing platform to all the marketing teams and bank branches. The app will be utilized by the marketing team for accurate customer selection. Reduced errors in identifying customers will <b>increase</b> the bank deposits. 

## System Environment
![](https://forthebadge.com/images/badges/made-with-python.svg)



[<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/e/ed/Pandas_logo.svg" width=200>](https://pandas.pydata.org/)     [<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/NumPy_logo_2020.svg/512px-NumPy_logo_2020.svg.png" width=200>](https://numpy.org/)     [<img target="_blank" src="https://www.fullstackpython.com/img/logos/scipy.png" width=200>](https://www.scipy.org/)                    



[<img target="_blank" src="https://www.metachris.com/images/posts/logzero/logo-text-wide-cropped.png" width=200>](https://pypi.org/project/logzero/)     [<img target="_blank" src="https://user-images.githubusercontent.com/965439/27257445-8791ea14-539c-11e7-8f5a-eec6cdfababa.png" width=200>](https://pypi.org/project/PyYAML/)     [<img target="_blank" src="https://phyblas.hinaboshi.com/rup/nayuki/2020/pythonsubprocess.png" width=200>](https://docs.python.org/3/library/subprocess.html)



[<img target="_blank" src="https://matplotlib.org/_static/logo2_compressed.svg" width=200>](https://matplotlib.org)     [<img target="_blank" src="https://seaborn.pydata.org/_static/logo-wide-lightbg.svg" width=200>](https://seaborn.pydata.org/)             



[<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" width=200>](https://scikit-learn.org)     [<img target="_blank" src="https://www.h2o.ai/wp-content/uploads/2018/07/xgboost-narrow.png" width=200>](https://github.com/dmlc/xgboost)     [<img target="_blank" src="https://lightgbm.readthedocs.io/en/latest/_images/LightGBM_logo_black_text.svg" width=200>](https://lightgbm.readthedocs.io/en/latest/)     [<img target="_blank" src="https://landscape.lfai.foundation/logos/cat-boost.svg" width=200>](https://catboost.ai/)    


[<img target="_blank" src="https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png" width=200>](https://streamlit.io/)     [<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Heroku_logo.svg/2560px-Heroku_logo.svg.png" width=200>](https://www.heroku.com/)

## Technical Description
The main project scripts are in the **"src"** directory. Exceptionally, **"app.py"** is in app directory. The main constituting scripts are as follows

* **get_data.py:** The script reads the data from **bank.csv** file located in data directory. The dataset is analyzed, cleaned and saved as **"cleaned_data.csv"** in **data** directory. 

* **data_analysis.py:** This script obtains various visualizations of the dataset. These visualizations are saved in the **"Visualization"** directory. 

* **prepare_data.py:** The script converts the required features to **categorical** variables. Subsequent outliers are determined using Grubb's Test. These outliers are removed and cleaned dataset is saved as **"prepared_data.csv"**.   

* **split_data.py:** The cleaned dataset is split using stratified sampling. This ensures the fair splitting. The train and test sets are obtained after dataset splitting. Labels are separated from train and test sets and saved as **"train_labels.csv"** and **"test_labels.csv"**. Train data and test data are respectively saved as **"train_set.csv"** and **"test_set.csv"**.

* **model_data.py:** Various data science models are trained on train set. Accuracy of all the models is verified using test set. Henceforth, the best model is selected. The feature selection of the best model is optimized to increase the accuracy to **87.1 %** (approx). This model is saved as **"model.pkl"**. 

* **app.py:** The script develops a Streamlit app; that accepts 16 user inputs. These inputs are transformed and fed to **model.pkl**. The model's prediction is displayed in the application. 
 
* **run_project.py:** The script runs all the project scripts (discussed in this section) sequentially. Therefore, entire project is executed with this script.  

**get_data_util.py**, **data_analysis_util.py**, **prepare_data_util.py**, **split_data_util.py**, **model_data_util.py** and **utility.py** declare vital functions that are required by respective scripts. 

## Directory Structure

```bash
├── app                              # Application files
|  ├── app.py                        # Application script
├── config                           # Configuration files
|  ├── config.yaml                   # Configuration file  
├── data                             # Data files ()   
|  ├── bank.csv                      # Bank customer dataset 
|  ├── clean_data.csv                # Cleaned dataset 
|  ├── prepared_data.csv             # Prepared dataset 
|  ├── train_set.csv                 # Train data
|  ├── test_set.csv                  # Test data
|  ├── train_label.csv               # Train labels
|  ├── test_set.csv                  # Test labels
├── log                              # Log files
|  ├── get_data.log                  # "get_data.py" script logs
|  ├── data_analysis.log             # "data_analysis.py" script logs
|  ├── prepare_data.log              # "prepare_data.py" script logs 
|  ├── split_data.log                # "split_data.py" script logs 
|  ├── model_data.log                # "model_data.py" script logs 
├── model                            # Model Files
|  ├── model.pkl                     # Saved model
├── src                              # Main project scripts 
|  ├── get_data.py                   # Dataset acquistion and cleaning script
|  ├── get_data_util.py              # script declaring utility functions for get_data.py 
|  ├── data_analysis.py              # Dataset analysis and visualization script
|  ├── data_anlaysis_util.py         # script declaring utility functions for data_analysis.py 
|  ├── prepare_data.py               # Dataset preperation script
|  ├── prepare_data_util.py          # script declaring utility functions for prepare_data.py 
|  ├── split_data.py                 # Dataset splitting script  
|  ├── split_data_util.py            # script declaring utility functions for split_data.py 
|  ├── model_data.py                 # Dataset modelling script
|  ├── model_data_util.py            # script declaring utility functions for model_data.py 
|  ├── utility.py                       # script declaring general utility functions  
├── visualizations                   # Dataset visualizations
|  ├── age_vs_deposit.png            # Age vs deposit figure
|  ├── bal_vs_deposit.png            # Balance vs deposit figure
|  ├── education_vs_deposit.png      # Education vs deposit figure
|  ├── job_vs_deposit.png            # Job vs deposit figure 
|  ├── marital_vs_deposit.png        # Marital vs deposit figure
|  ├── dataset_balance.png           # Dataset balance figure
|  ├── correlation_heatmap.png       # Correalation heatmap of features
|  ├── feature_importance.png        # Feature importance of best model
|  ├── cm_etc.png                    # Confusion matrix of ExtraTreesClassifier
|  ├── cm_gbc.png                    # Confusion matrix of GradientBoostClassifier
|  ├── cm_lgbm.png                   # Confusion matrix of LightGBMClassifier
|  ├── cm_rfc.png                    # Confusion matrix of RandomForestClassifier
|  ├── cm_xgb.png                    # Confusion matrix of XGBClassifier  
|  ├── cm_cbc.png                    # Confusion matrix of CatBoostClassifier
|  ├── cm_optimized_cbc.png          # Confusion matrix of optimized CatBoostClassifier
├── requirements.txt                 # Required libraries
├── Procfile                         # Required for Heroku deployment 
├── setup.sh                         # Required for Heroku deployment
├── LICENSE                          # License
├── README.md                        # Repository description

```

## Installing Dependencies
Foremost running the project, installing the dependencies is essential. 
* Ensure Python 3.8.8 or later is installed in the system. 
* All required libraries are listed in "requirements.txt". These are easily installed; by running the following command in project directory
```bash
pip install -r requirements.txt
```

## Run Project
As discussed in **Technical Aspect** section, "src" and “app” directory possess the main scripts. 

Running the following command in the "src" directory executes the entire project  
```bash
python3 run_project.py
```
Alternatively, a project script can be individually executed using the general script 
```bash
python3 script.py
```
Here “script.py” represents any python script. 

Exceptionally, application file "app.py" runs using command 
```bash
streamlit run app/app.py
```
**Note:** To run any project script, directory location must be correct.
   

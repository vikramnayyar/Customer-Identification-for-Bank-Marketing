# Customer Identification for Bank Marketing Campaign

## Demo
The application is deployed in Heroku. The app is available in the following link
https://depositing-customers-in-bank.herokuapp.com/

## Introduction
An app is developed for bank marketing campaigns; that target customers interested in making term deposits. App is based on 15 inputs that predict wheather a customer will deposit or not? The app was trained using <b>sklearn</b> models and is developed in <b>Streamlit</b>. 

## Dataset
The dataset consists of actual information obtained from a marketing campaign of a Portuguese banking institution. The bank launched this campaign to increase the term deposits. Often; each customer was contacted more than once, to determine as a depositor or non-depositor.

The dataset was acquired from Kaggle and was uploaded by Janio Martinez Bachmann (Datasets Grandmaster). This consists <b>11162</b> rows and <b>15</b> features.    

## Problem Statement
Marketing a product or a service is very challenging. Identifying the right customer is vital for the marketing team. This can significantly reduce the resources and time. Furthermore, this allows the team to position the product correctly. Unfortunately, finding the right customer can be exhaustive and complicated. There are many features to consider and huge data to analyze. Henceforth, the marketing team relies on experience of the marketing experts and feedback of team. 

Due to vast facts originating from so many features; a mistake in identification of customer is inevitable. Missing a customer segment results as a loss to the institution. On contrary, identifying wrong segment of customers will result in wastage of resources and time (As faults in strategy is confirmed at a later stage).
Besides; human error is highly probable and often unnoticeable. 

Therefore, such a project is vital for product marketing. 

## Goal
This work was performed as a personal project and is based on the dataset available on kaggle. The motivation was to obtain analysis of bank marketing campaign and identify customers the will make term deposits. For highest possible term deposits, a high accuracy was desirable for customer classification.   

An app classifying depositing customers, provides a very straightforward and intuitive means for identifying customers. This saves substantial <b>resources</b> and <b>time</b>. Also, this apporach is easily reproducible, thus; provides a <b>common</b> marketing platform to all the marketing teams and bank branches. The app will be utilized by the marketing team for accurate customer selection. Reduced errors in identifying customers will <b>increase</b> the bank deposits. With 15 features, the app should be prefilled with usual values.  

## Technical Description
The main constituents of this work are as follows
#### Exploratory Data Analysis 
Various analysis were performed to highlight different feature dependencies on deposits. 

#### Outlier Removal 
Outliers were identified using <b>Grubbs Test</b>. Using scaling or value replacements the outliers were eliminated. 

#### Feature Selection 
Using correlation few features were removed. These features had negigible correlation and were found degrading the accuracy.  

#### Feature Addition 
With absence of a strong feature, two features were designed that posessed highest positive and negative correlations. 

#### Training & Testing Classifiers 
After train-test splitting, ExtraTreesClassifier, AdaBoostClassifierm BaggingClassifier, GradientBoostingClassifier, RandomForestClassifier, DecisionTreeClassifier, CatBoostClassifier, XGBoostClassifier and LGBMClassifier were trained and tested. 

#### Best Model Selection & Improvement 
CatBoostClassifier was determined to be the best model. This model was selected and its accuracy was further improved by important <b>feature selection</b> and manual <b>parameter tuning</b>. 

#### Web Application 
Using the trained model, an app was developed in <b>streamlit</b>. This app predict customers that will make deposits. A marketing individual can easily select a number of features to identify such customers. Furthermore, for convinience; app fields are prefilled with average values.   

Final accuracy of <b>87.7%</b> was achieved. Among 85 kaggle notebooks, this was the highest achieved accuracy (Kaggle Notebook Link: https://www.kaggle.com/janiobachmann/bank-marketing-dataset/code).  

## Directory Structure


## Installing Dependencies
The model was developed in Python 3.8.8. All the libraries used in modelling can be easily installed; by running the following command in project directory
```bash
pip install -r requirements.txt
```
requirements.txt possesses the list of all required libraries.  

#### Running Streamlit App



## Run Streamlit Web App from Github 
Running the streamlit web app is very simple. Please execute the following command on the terminal (for Ubuntu users) or command prompt (for Windows or Mac users) 
```bash
streamlit run 
```

## Libraries Used

![](https://forthebadge.com/images/badges/made-with-python.svg)


[<img target="_blank" src="https://www.fullstackpython.com/img/logos/scipy.png" width=200>](https://www.scipy.org/)     [<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/NumPy_logo_2020.svg/512px-NumPy_logo_2020.svg.png" width=200>](https://numpy.org/)     


[<img target="_blank" src="https://matplotlib.org/_static/logo2_compressed.svg" width=200>](https://matplotlib.org)     [<img target="_blank" src="https://seaborn.pydata.org/_static/logo-wide-lightbg.svg" width=200>](https://seaborn.pydata.org/)   



[<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" width=200>](https://scikit-learn.org)     [<img target="_blank" src="https://www.h2o.ai/wp-content/uploads/2018/07/xgboost-narrow.png" width=200>](https://github.com/dmlc/xgboost)     [<img target="_blank" src="https://lightgbm.readthedocs.io/en/latest/_images/LightGBM_logo_black_text.svg" width=200>](https://lightgbm.readthedocs.io/en/latest/)     [<img target="_blank" src="https://landscape.lfai.foundation/logos/cat-boost.svg" width=200>](https://catboost.ai/)    


[<img target="_blank" src="https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png" width=200>](https://streamlit.io/)     [<img target="_blank" src="https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png" width=200>](https://streamlit.io/)

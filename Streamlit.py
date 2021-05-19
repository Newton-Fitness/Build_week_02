#%%
#Imports
import pandas as pd
import chime
import streamlit as st

## Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import sklearn as skl
import time
from IPython.display import display, clear_output
#from ctgan import CTGANSynthesizer
import sklearn
from sklearn import pipeline      # Pipeline
from sklearn import preprocessing # OrdinalEncoder, LabelEncoder
from sklearn import model_selection # train_test_split
from sklearn import metrics         # accuracy_score, balanced_accuracy_score, plot_confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import chime



#%%
#Load data
#original_data = pd.read_csv("heart.csv")
#new_data = pd.read_csv("New_Data.csv")	

#%%
#Preprocess data
#%% md

## boxplot from blood pressure (trestbps)

#%%

import pickle


### streamlit code
#st.title(f"This machine Learning Model has accuracy score of {acc_score}")
st.text("Newton Fitness app")

a = pd.read_csv("input.csv")
filename = 'model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
y_pred=loaded_model.predict(a)
st.text(y_pred)
#st.text(type(y_pred))
a = pd.read_csv("input.csv")
y_pred=loaded_model.predict(a)

#Model
# simple model

#print(final)
#predict = model.predict(final)
#print(predict)

#st.text(type(predict))

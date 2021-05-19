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
original_data = pd.read_csv("heart.csv")
new_data = pd.read_csv("New_Data.csv")	

#%%
#Preprocess data
#%% md

## boxplot from blood pressure (trestbps)

#%%
stats = original_data.trestbps.describe()
#low range = below 25% normal = 25% < 75%  high = above 75%
var_min, var_max, var_25, var_75 = stats[3], stats[7], stats[4], stats[6]

#%% md
## encoding blood pressure
#%%
#creating new column for classifying blood pressure:
# 0 = low, 1 = normal, 2 = high
df = original_data
for row in df.trestbps:
    if row < var_25:
        df['trestbps_encoded'] = 0
    elif var_25 < row < var_75:
        df['trestbps_encoded'] = 1
    elif var_75 < row:
        df['trestbps_encoded'] = 2

#Adding default values
#age = 20
#Inputs
from sklearn.model_selection import train_test_split

train_data = pd.read_csv("heart.csv") #pd.read_csv('../input/scikitconf/heart-disease.csv')
x=train_data.drop(columns="target",axis=1)
y=train_data[["target"]]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=40,stratify = y)

scaler = MinMaxScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.transform(x_test)
model = KNeighborsClassifier()
model.fit(x_train,y_train)
acc_score = model.score(x_test,y_test)
acc_score = round(acc_score,3)


### streamlit code
st.title(f"This machine Learning Model has accuracy score of {acc_score}")
st.text("Enter your infos")

age = st.text_input('Age', 29)
sex = st.text_input('Sex',1)
cp = st.text_input('Chest Pain',3)
trestbps = st.text_input('Blood pressure',94)
chol = st.text_input('Cholesterine level',126)
fbs = st.text_input('Fasting blood sugar',1)
restecg = st.text_input('Resting Electrokardiographical result',0)
thalach = st.text_input('Maximum heart rate',150)
exang = st.text_input('Exercise includes Angina',0)
oldpeak = st.text_input('Oldpeak',2.3)
slope = st.text_input('Slope',0)
ca = st.text_input('Number of major vessels',0)
thal = st.text_input('Thal',2)

#Model
# simple model

age = 29
sex = 1
cp = 3
trestbps = 94
chol = 126
fbs = 1
restecg = 0
thalach = 150
exang = 0	
oldpeak = 2.4
slope = 0
ca = 0
thal = 1
arr = np.array([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]) 
singledf = pd.DataFrame(arr)
final = singledf.transpose()
#print(final)
predict = model.predict(final)
print(predict)

#st.text(type(predict))

if predict == 0:
	chime.success()
	chime.success()
	chime.success()
	chime.info()
	st.text("heart is goods")
else:
	chime.warning()
	chime.warning()
	chime.warning()
	chime.error()
	st.text("consult doctor")


#train_data = pd.read_csv("heart.csv")
st.text(f"The given shape of the data is {original_data.shape}\n")
st.text(f"The new shape of the data is {new_data.shape}\n")


st.markdown("""
<style>
body {
    color: #fff;
    background-color: #111;
}
</style>
    """, unsafe_allow_html=True)

#print("\tpredicted output:",predict)
#Predict
#my_y = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
#st.text(20)

#print(my_y)
#st.dataframe(predict)
#predict = model.predict(my_y)
#pred_proba = model.predict_proba(my_y)
#print(type(y_test))
#Display prediction with sound
#audio_file = open('example.mp3', 'rb').read()

#




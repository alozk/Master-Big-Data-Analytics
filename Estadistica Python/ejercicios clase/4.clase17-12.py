# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 15:36:24 2021

@author: alvar
"""

#Importamos todas las librerias necesarias para el proyecto

import os                           #sistema operativo
import pandas as pd                 #gestionar datframes
import numpy as np                  #numeric python vectores
import matplotlib.pyplot as plt     #graficos estadisticos
from pandas.api.types import CategoricalDtype #For definition of custom categorical data types (ordinal if necesary)
import seaborn as sns  # For hi level, Pandas oriented, graphics
import scipy.stats as stats  # For statistical inference
from statsmodels.formula.api import ols
from stargazer.stargazer import Stargazer     #para modelos de regresion


os.chdir(r'C:\Users\alvar\Desktop\EDEM\2. GITHUB\edem\Estadistica Python\code_and_data\datasets')
wbr = pd.read_csv ('WBR_11_12_denormalized_temp.csv', sep=';', decimal=',')
os.getcwd()
print(wbr.shape)
print(wbr.head())
print(wbr.info())
#Quality Control OK
#OLS Ordinary least squares


#(variable target ~variable predictora).fit(ajusta la recta)
model1=ols('cnt~temp_celsius',data=wbr).fit() 
model2=ols('cnt~temp_celsius+windspeed_kh',data=wbr).fit()
model3=ols('cnt~temp_celsius+windspeed_kh+hum',data=wbr).fit()
model4=ols('cnt~temp_celsius+windspeed_kh+hum+yr',data=wbr).fit()
model5=ols('cnt~temp_celsius+windspeed_kh+hum+workingday+yr',data=wbr).fit()
print(model5.summary2())

#!pip install stargazer
stargazer = Stargazer([model1, model2,model3])
stargazer.render_html()


stargazer = Stargazer([model1, model2,model3,model4,model5])
stargazer.title('Table 1. A model of bicycle demand in Washington')
stargazer.significant_digits(1)
stargazer.covariate_order(['temp_celsius', 'windspeed_kh','hum','yr','workingday'])
stargazer.show_degrees_of_freedom(False)
stargazer.render_html()

#Get dummies / hot encoding

wbr.weathersit.hist()
wbr

dummies = pd.get_dummies(wbr.weathersit)
colnames = { 1:'sunny', 2:'cloudy', 3:'rainy'} #This is a dictionary

dummies.rename(colnames, inplace = True, axis=1) #Rename column labels
wbr = pd.concat([wbr,dummies],axis=1) #add new columns

wbr.columns
#recomendacion siempre en binario a las variables dicotomicas

#la mayoria de los dias hace sol
model6 = ols('cnt~temp_celsius + hum + workingday + windspeed_kh + yr + cloudy +rainy', data=wbr).fit()

#################off road regression
m=4500
print(m)
wbr.loc[(wbr['cnt']<m), 'goal']=0
wbr.loc[(wbr['cnt']>m), 'goal']=1

plt.scatter(wbr.cnt, wbr.goal)

from statsmodels.formula.api import logit
model_l1 = logit('goal ~ temp_celsius', data=wbr).fit()
print(model_l1.summary2())

model_l7 = logit('goal~temp_celsius + hum + workingday + windspeed_kh + yr + cloudy +rainy', data=wbr).fit()
print(model_l7.summary2())

#la temp2 sale con decimales, se puede considerar redondear
wbr['temp2'] = wbr.temp_celsius*wbr.temp_celsius
wbr['temp2b'] = wbr.temp_celsius**2


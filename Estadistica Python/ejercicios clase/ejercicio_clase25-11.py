# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 18:59:58 2021

@author: alvar
"""

#Percentage Comparison
#MDA EDEM

#Resets ALL (Careful This is a "magic" function then it doesn't run as script) 
#reset -f   

#load basiclibraries
import os
import numpy as np
import pandas as pd
from pandas.api.types import CategoricalDtype #For definition of custom categorical data types (ordinal if necesary)
import matplotlib.pyplot as plt
import seaborn as sns  # For high level, Pandas oriented, graphics
import scipy.stats as stats  # For statistical inference 


#Reads data from CSV file and stores it in a dataframe called rentals_2011
# Pay atention to the specific format of your CSV data (; , or , .)
os.chdir(r'C:\Users\alvar\Desktop\stat_python\code_and_data\data_session_1_3\data_1_3')
os.getcwd()
wbr = pd.read_csv (r"WBR_11_12_denormalized_temp.csv", sep=';', decimal=',')
wbr.shape
wbr.head()
#QC OK


#Recoding DV for analysis
res = wbr.cnt.describe()
print (res)
# Store parameters as numbers
m  = res[1]
sd = res[2]
n  = res[0]

### Recode cnt to string
wbr.loc[  (wbr['cnt']<(m-sd)) ,"cnt_str"]= "Low rentals"
wbr.loc[ ((wbr['cnt']>(m-sd)) & (wbr['cnt']<(m+sd))) ,"cnt_str"]= "Average rentals"
wbr.loc[  (wbr['cnt']>(m+sd)) ,"cnt_str"]= "High rentals"

### Recode cnt to ordinal
my_categories=["Low rentals", "Average rentals", "High rentals"]
my_rentals_type = CategoricalDtype(categories=my_categories, ordered=True)
wbr["cnt_cat"] = wbr.cnt_str.astype(my_rentals_type)
wbr.info()

#frequencies & barchart
mytable = pd.crosstab(wbr.cnt_cat, columns="count", normalize='columns')*100
print(mytable)
print (round(mytable,1))
plt.bar(mytable.index, mytable['count'])

#######################
# Recode  working day
# To string
wbr["wd_st"] = wbr.workingday
wbr.wd_st = wbr.wd_st.replace(to_replace=0, value="No")
wbr.wd_st = wbr.wd_st.replace(to_replace=1, value="Yes")
#To category
my_categories=["No","Yes"]
my_datatype = CategoricalDtype(categories=my_categories, ordered=True)
wbr["wd_cat"] = wbr.wd_st.astype(my_datatype)
wbr.info()

# Barchart for Working day
mytable = pd.crosstab(index=wbr["wd_cat"], columns="count") # Crosstab
n=mytable.sum()
mytable2 = (mytable/n)*100
print(mytable2)
plt.bar(mytable2.index, mytable2['count'])
plt.xlabel('Working Day')
plt.title('Figure 5. Percentage of Working Days')


#Crosstabulation
pd.crosstab(wbr.cnt_cat, margins=True) #1er La VD Traget 2da La predictora o VI
pd.crosstab(wbr.cnt_cat, wbr.wd_cat, normalize='columns', margins= True)*100

my_ct=pd.crosstab(wbr.cnt_cat, wbr.wd_cat, normalize='columns', margins= True)*100
my_ct

round (my_ct, 1) #Function
my_ct.round(1) #Objeto . metodo

my_ct = round(my_ct, 1)
my_ct

#Statistical test
ct=pd.crosstab(wbr.cnt_cat, wbr.wd_cat)

#tabla de contingencia solo con las dos variables, sin total y sin porcentajes, solo frecuencia
stats.chi2_contingency(ct)

#ploting the cross tabulation
my_ct.plot(kind='bar') #carefull this is not what we want
my_ct.Tplot(kind='bar')


#transpose and plot
my_ct2=my_ct.transpose()

#my_ct2=my_ct.T.plot(kind='bar')
my_ct.plot(kind='bar')
my_ct.plot(kind='bar', edgecolor='black')

my_ct.plot(kind='bar', edgecolor='black', colomap='Paired')
my_ct.plot(kind='bar', edgecolor='black', colomap='Blues')

my_ct.plot(kind='bar', edgecolor='black', colomap='Greens')




my_ct.plot(kind='bar', edgecolor='black', colomap='Blues')
plt.ylim(0,100)
props=dict(boxstyle='round', facecolor='white', lw=0.5)

plt.legend(['Low rentals', 'Average rentals', 'High rentals'])
plt.text(-0.4,81, 'Chi2: 4.983''/n''n: 731' 'n' 'Pval.: 0.083', bbox=props)#contrabarra
plt.xlabel('Working Day')
plt.title('Figure 7. Percentage of Rental level, by Working Day''/n')
plt.xticks(rotation='horizontal')

plt.savefigs('cross_tab_plot3.eps')


my_ct.plot(kind='bar', edgecolor='black', colomap='Paired')




#############EJERCICIO DURANTE LA CLASE

#Recode working day
#To string
wbr['wbr_st']=wbr.weathersit
wbr.wd_st = wbr.wd_st.replace(to_replace=1, value='Sunny')
wbr.wd_st = wbr.wd_st.replace(to_replace=2, value='Cloudy')
wbr.wd_st = wbr.wd_st.replace(to_replace=3, value='Rainy')
#To category
my_categories=['Sunny', 'Cloudy', 'Rainy']
my_datatype= CategoricalDtype(categories=my_categories, ordered=True)
wbr['wd_cat']=wbr.wd_st.astype(my_datatype)
wbr.info()

#Barchart for working day
mytable = pd.crosstab(index=wbr['wd_cat'], columns='count') #Crosstab
n=mytable.sum()
mytable2=(mytable/n)*100
print(mytable2)
plt.bar(mytable2.index, mytable2['count'])
plt.xlable('Working day')
plt.title('Figure 5. Percentage of Working Days')
plt.show()

'''
ct=pd.crosstab(wbr.cnt_cat, wbr.wd_cat
myct=pd.crosstab(wbr.cnt_cat,normalize='columns', margins=True)
print(myct)
print(stats.chi2_contingency(ct))

myct=myct.transpose()

myct2.plot(kind='bar')
plt.ylim(0,100)
'''
































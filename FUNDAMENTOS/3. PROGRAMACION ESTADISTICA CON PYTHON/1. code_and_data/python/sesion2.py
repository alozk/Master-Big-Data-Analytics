# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Clase 1 - Estadistica con Python

#reset -f

import os                           #sistema operativo
import pandas as pd                 #gestionar datframes
import numpy as np                  #numeric python vectores
import matplotlib.pyplot as plt     #graficos estadisticos
import seaborn as plt
#creamos lista de clase

name = ['Alvaro', 'Hector', 'Luis', 'Ismail', 'Ana']
age = [24,27,23,22,18]
gender = ['Male','Male','Male','Male','Female']

print(name, age, gender)

class2021 = pd.DataFrame({'name':name, 'age':age, 'gender':gender})

#clean up
del (age,gender,name)

class2021.shape
class2021.head(3)
class2021.tail(2)

class2021.head()
class2021.tail()

#Quality control OK

edad = class2021.age
del(edad)

#get working directory
os.chdir(r'C:\Users\alvar\Desktop\stat_python\code_and_data\data_session_1_3\data_1_3')
rentals_2011 = pd.read_csv ('Washington_bike_rentals_2011.csv', sep=';', decimal=',')
os.getcwd()

rentals_2011.shape
rentals_2011.head()
rentals_2011.tail()

#QC OK

rentals_2011.cnt
np.mean (rentals_2011.cnt)
np.std (rentals_2011.cnt)

rentals_2011.cnt.mean()
rentals_2011.cnt.describe()

#histrograma
plt.hist(rentals_2011.cnt)

#datos cuantitativos (media, desviacion tipica e histograma[graficamente])

#plot
x=rentals_2011['cnt']
x=rentals_2011.cnt      #es lo mismo que la linea anterior

plt.hist(x,edgecolor='black',bins=20)
plt.xticks(np.arange(0, 10000, step=1000))
plt.title("Figure 1. Registered rental")
plt.ylabel('Frecuencia')
plt.xlabel('Number of rentals')
plt.show()

#importamos clima
weather_2011 = pd.read_csv ('weather_washington_2011.csv', sep=';',decimal=',')

weather_2011.shape
weather_2011.dtypes

#merge the two dataframes into a new one
rentals_weather_2011 = pd.merge(weather_2011, rentals_2011, on='day')

rentals_weather_2011.shape
rentals_weather_2011.head()

print(rentals_weather_2011.dtypes)
print(rentals_weather_2011.describe)

#date is duplicated, remove second version
del(rentals_weather_2011['dteday_y'])

rentals_weather_2011 = rentals_weather_2011.rename(columns={"dteday_x":"dteday"})

#WEATHER 2012
#add new cases (rows) to DATAFRAME
#Read cases from anpother year (2012) in a new
rentals_weather_2012 = pd.read_csv("rentals_weather_2012.csv", sep=";", decimal=",")

#MERGE


rentals_weather_11_12 = rentals_weather_2011.append(rentals_weather_2012, ignore_index=True)

wbr=rentals_weather_11_12

#frequencies

mytable = wbr.groupby(['weathersit']).size()
print(mytable)

n=mytable.sum()

mytable2 = (mytable/n)*100
print(mytable2)

mytable3 = round(mytable2,1)
print(mytable3)
'''
#barchart1
#lets label the cathegories
bar_list = ['Sunny', 'Cloudy', 'Rainy']
plt.bar(bar_list, mytable2)
'''
#barchart2
#lets label the cathegories
bar_list = ['Sunny', 'Cloudy', 'Rainy']
plt.bar(bar_list, mytable2, edgecolor='black')
plt.ylabel('Percentage')
plt.title('Figure 1. Percentage of weather situation')
plt.text(1.7, 50,'n:731')

#save pics

plt.savefig('bar1.eps') #Edit Adobe Illustrator
plt.savefig('bar1.jpg') #Foto no edit
plt.savefig('bar1.svg')

wbr = pd.read_csv ('WBR_11_12_denormalized_temp.csv', sep=';', decimal=',')
wbr.shape
print(wbr.tail())

#Vende el proyecto
print(wbr.cnt.describe())

#select the variable to plot

x=wbr['cnt']


#plot

plt.hist(x, edgecolor='black')
ticks=np.arange(0,10000,1000)
plt.xticks(ticks)


# plot in white

#histogram Figure 1
plt.hist(x, bins=10, edgecolor='black')
plt.xticks(np.arange(0,10000, step=1000))
plt.title('Figure 1. Daily Bicycle rentals in Washington')
plt.ylabel('Frequency')
plt.xlabel('Number of rented bicycles')
plt.show()










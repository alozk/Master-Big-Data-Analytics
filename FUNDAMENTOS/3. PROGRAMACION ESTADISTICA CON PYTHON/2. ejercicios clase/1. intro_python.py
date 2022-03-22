#Clase 1 - Estadistica con Python

#reset -f
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
os.getcwd()
os.chdir('C:/Users/alvar/Desktop/Estadistica Python')

#Save dataframe to Excel
class2021.to_excel("class2021.xlsx")
class2021.to_csv("class2021.csv")

rentals_2021 = pd.read_csv ('Washington_bike_rentals_2011.csv')
os.chdir(r'C:\Users\alvar\Desktop\Estadistica Python\code_and_data')
print(os.getcwd)

rentals_2011.shape
rentals_2011.head()
rentals_2011.tail()

#QC OK

rentals_2011.cnt
np.mean (rentals_2021.cnt)
np.std (rentals_2021.cnt)

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























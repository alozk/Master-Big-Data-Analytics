# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 19:03:24 2021

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

#Mencionamos carpeta donde se encuentra nuestro csv y lo mencionamos con el nombre "heart"
#Reads data from CSV file and stores it in a dataframe called rentals_2011
#Pay atention to the specific format of yout CSV data (; , or , .)

os.chdir(r'C:\Users\alvar\Desktop\EDEM\2. GITHUB\edem\Estadistica Python\code_and_data\datasets')
wbr = pd.read_csv ('WBR_11_12_denormalized_temp.csv', sep=';', decimal=',')
os.getcwd()
print(wbr.shape)
print(wbr.head())
print(wbr.info())
#Quality Control OK

##################TEMPERATURE
#Temperature describe
res = wbr['temp_celsius'].describe()
#Store parameters as numbers
m = res[1]
sd = res[2]
n = res[0]

#Temperature Histogram
x = wbr['temp_celsius']
plt.hist(x, bins=10, edgecolor='black')
#plt.xticks(np.arange(0,10000,step=1000))
plt.title('Figure 5. Temperature in Celsius')
plt.ylabel('Frequency')
plt.xlabel('Temperature in Cº')
props = dict(boxstyle='round', 
             facecolor='white', 
             lw=0.5)
textstr = '$\mathrm{n}=%.0f$'%(n)
plt.text (2,100, textstr, bbox=props)
plt.axvline(x=m,
            linewidth=1,
            linestyle= 'solid',
            color="red",
            label='Mean')
plt.axvline(x=m-sd,
            linewidth=1,
            linestyle= 'dashed',
            color="green",
            label='- 1 S.D.')
plt.axvline(x=m + sd,
            linewidth=1,
            linestyle= 'dashed',
            color="green",
            label='+ 1 S.D.')

###################Scatterplot
###Eje y = temperatura  Eje x ventas
#Primero la variable predictora y luego la predicha
plt.scatter (wbr.temp_celsius, wbr.cnt)
plt.ylabel('# Daily Rentals')
plt.xlabel('Temperature (Cº)')




x=wbr.temp_celsius
y=wbr.cnt
tit='Figure 9.Daily bicycle rental, by temperature.''\n'
plt.figure(figsize=(5,5))

#si es muy denso, para ver los huecos y visualizar con facilidad
plt.scatter(x,y, s=20, facecolors='none', edgecolors='C0')
#plt.xticks(np.arange(0, 11, step=1))
plt.ylabel('# Daily Rentals')
plt.xlabel('Temperature Cº')
plt.show()

#Que estadistico mide la asociacion entre dos cuantitativas 
###Correlation [lineal], que se hace con pearsonr (de -1 a +1) 
from scipy.stats.stats import pearsonr

x=wbr.temp_celsius
y=wbr.cnt
pearsonr(x,y)


r, p_val=pearsonr(x,y)

print(r,p_val)

n=len(wbr.cnt) #necesitamos el tamaño muestral [n]
print ('r:', round(r,3), 'P.Val:', round(p_val,3), 'n:', n)



###Include correlation result into plot 
plt.figure(figsize=(5,5))
plt.scatter(x,y, s=20, facecolors='none', edgecolors='C0')
plt.xticks(np.arange(0, 40, step=5))
plt.yticks(np.arange(0, 10000, step=1000))
plt.title("figura 4.Dailly bicycle rentals, by temperature")
plt.ylabel('# Daily Rentals')
plt.xlabel('Temperature in Cº')
props=dict(boxstyle='round', facecolor='white', lw=0.5)
textstr= '$\mathrm{r}=%.2f$\n$\mathrm{P.Val:}=%.3f$\n$\mathrm{n}=%.0f$'%(r, p_val, n)
plt.text (3,7000, textstr , bbox=props)
plt.show()
#textstr viene de Latex


####Mirar si la separacion de grupos del scattr se debe a el año
#hemos cambiado el color en c=wbr.yr
plt.figure(figsize=(5,5))
plt.scatter(x,y, s=20, facecolors='none', c=wbr.yr)
plt.xticks(np.arange(0, 40, step=5))
plt.yticks(np.arange(0, 10000, step=1000))
plt.title("figura 5.Dailly bicycle rentals, by temperature in years 2011-2012")
plt.ylabel('# Daily Rentals')
plt.xlabel('Temperature in Cº')
props=dict(boxstyle='round', facecolor='white', lw=0.5)
textstr= '$\mathrm{r}=%.2f$\n$\mathrm{P.Val:}=%.3f$\n$\mathrm{n}=%.0f$'%(r, p_val, n)
plt.text (3,7000, textstr , bbox=props)
plt.show()

#Hemos cambiado el color en c=wbr.season (para diferenciar estaciones)
plt.figure(figsize=(5,5))
plt.scatter(x,y, s=20, facecolors='none', c=wbr.season)
plt.xticks(np.arange(0, 40, step=5))
plt.yticks(np.arange(0, 10000, step=1000))
plt.title("figura 5.Dailly bicycle rentals, by temperature in years 2011-2012")
plt.ylabel('# Daily Rentals')
plt.xlabel('Temperature in Cº')
props=dict(boxstyle='round', facecolor='white', lw=0.5)
textstr= '$\mathrm{r}=%.2f$\n$\mathrm{P.Val:}=%.3f$\n$\mathrm{n}=%.0f$'%(r, p_val, n)
plt.text (3,7000, textstr , bbox=props)
plt.show()


#Windspeed
x=wbr.windspeed_kh
y=wbr.cnt
r, p_val = pearsonr(x,y)
n = len (wbr.cnt)
tit ='Figure. Daily bicycle rentals, by windspeed ''\n'


plt.figure(figsize=(5,5))
plt.scatter(x,y, s=20, facecolors='none', c='C0')
#plt.xticks(np.arange(0, 11, step=1))
plt.yticks(np.arange(0, 10000, step=1000))
plt.title("figura 5.Dailly bicycle rentals, by temperature in years 2011-2012")
plt.ylabel('# Daily Rentals')
plt.xlabel('Windspeed')
props=dict(boxstyle='round', facecolor='white', lw=0.5)
textstr= '$\mathrm{r}=%.2f$\n$\mathrm{P.Val:}=%.3f$\n$\mathrm{n}=%.0f$'%(r, p_val, n)
plt.text (25,7000, textstr , bbox=props)
plt.show()


#################################ADITIONAL
#Set sumber of columns
n=100

#Create a dataset with 1000 random int number (from 0 to 100)
df1 = pd.DataFrame (np.random.randint(0,100, size=(1000, n)), columns=np.arange(1,n+1,1))
print (df1)

plt.scatter(df1[1], df1[2])
pearsonr(df1[1], df1[2])

#Compute the correlations btw all variables
c_m= df1.corr()
corr_matrix=df1.corr()
print (c_m)

#represent the correlation matrix in a heatmap
#sns.heatmap(c_m, vmin=-1, vmax=1, center=0, cmpa=sns.diverging_palette(20, 220, n=200)), square=True

#Fine-tune graphic parameter (ranges of color scale)
sns.heatmap(c_m, vmin=-0.2, vmax=0.2, center=0, cmap= 'coolwarm', square=True)

#Now compute the p-values for every correlation to learn wich correlations are significant

#For doing so I create a specific function for that (functions will be discussed later in the)

def calculate_pvalues(df):
        df = df.dropna()._get_numeric_data()
        dfcols = pd.DataFrame(columns=df.columns)
        pvalues = dfcols.transpose().join
        for r in df.columns:
            for c in df.columns:
                pvalues[r][c] = round(pearsonr(df[r], df[c])[1],4)
        return pvalues

#Get the p_values matrix and transform it to numeric, so we can rank them later
p_val_matrix = calculate_pvalues(df1)
col=np.arange(1,n+1,1)
p_val_matrix[col] = pd.to_numeric(p_val_matrix[col].stack(), errors='coerce').unstack()

#Let's take all the p_values and let's rank them in a list
list_pval = (p_val_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool))
             .stack()
             .sort_values(ascending=False))


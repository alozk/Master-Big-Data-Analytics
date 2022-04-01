# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 18:17:34 2021

@author: alvar
"""
#Importamos todas las librerias necesarias para el proyecto

import os                           #sistema operativo
import pandas as pd                 #gestionar datframes
import numpy as np                  #numeric python vectores
import matplotlib.pyplot as plt     #graficos estadisticos


#Mencionamos carpeta donde se encuentra nuestro csv y lo mencionamos con el nombre "heart"
os.chdir(r'C:\Users\alvar\Desktop\EDEM\2. GITHUB\edem\Estadistica Python\my project')
heart = pd.read_csv ('heart.csv', sep=',')
os.getcwd()

#A continuación comprobamos que se ejecuta
print(heart)

#Sacamos datos estadísticos como la media, desviacion tipica y quartile
print(heart.head(4))
#Hacemos describe para las variables nominales identificadas
print(heart.Sex.describe())
print(heart.ChestPainType.describe())
print(heart.RestingECG.describe())
print(heart.ExerciseAngina.describe())
print(heart.ST_Slope.describe())

#Hacemos describe para las variables cuantitativas identificadas
Age = heart.Age.describe()
print(heart.Age.describe())
m_age=Age[1]
sd_age=Age[2]
print(m_age)

print(heart.RestingBP.describe())

Cholesterol = heart.Cholesterol.describe()
print(heart.Cholesterol.describe())
m_cho=Cholesterol[1]
sd_cho=Cholesterol[2]

print(heart.FastingBS.describe())
print(heart.MaxHR.describe())
print(heart.Oldpeak.describe())
print(heart.HeartDisease.describe())


#TABLAS
#Creamos una tabla para 3 variables nominales
#Nominal tipo Sex
mytablesex = heart.groupby(['Sex']).size()
print(mytablesex)
n=mytablesex.sum()

#Sacamos la tabla con porcentajes
mytablesex2 = (mytablesex/n)*100
print(mytablesex2)

#Redondeamos los porcentajes
mytablesex3 = round(mytablesex2,1)
print(mytablesex3)

#Nominal tipo: ChestPainType
mytablechest = heart.groupby(['ChestPainType']).size()
print(mytablechest)
n=mytablechest.sum()

#Sacamos la tabla con porcentajes
mytablechest2 = (mytablechest/n)*100
print(mytablechest2)

#Redondeamos los porcentajes
mytablechest3 = round(mytablechest2,1)
print(mytablechest3)

#Identificamos y elegimos la variable Sexo como nominal
#Creamos una tabla con la variable Sexo
mytable = heart.groupby(['Sex']).size()
print(mytable)
n=mytable.sum()

#Sacamos la tabla con porcentajes
mytable2 = (mytable/n)*100
print(mytable2)

#Redondeamos los porcentajes
mytable3 = round(mytable2,1)
print(mytable3)

#Una vez creada la tabla, creamos su plot
n=mytable.sum()

bar_list = ['ASY', 'ATA', 'NAP', 'TA']
plt.bar(bar_list, mytablechest3, edgecolor='black')
plt.ylabel('Percentage')
plt.xlabel('Chest Pain Type')
plt.title('Figure 4. Percentage of Chest Pain Type')
props = dict(boxstyle='round', facecolor='white', lw=0.5)
textstr = '$\mathrm{n}=%.0f$'%(n)
plt.text(1.6, 50,'n:918')



plt.savefig('Figure 4.svg')

#Para evitar que se junten dos gráficas, ejecutamos otra vez:
plt.show()

#Una vez creada la tabla, creamos su plot
n=mytable.sum()
bar_list = ['Female', 'Male']
plt.bar(bar_list, mytablesex3, edgecolor='black')
plt.ylabel('Percentage')
plt.xlabel('Sex')
plt.title('Figure 3. Percentage of Female and Male')
plt.text(1.5, 50,'n:918')
#Observamos visualmente en el plot como:
#las Mujeres son el 21% y hombres el 79% del sample de 918 pacientes
plt.savefig('Figure 3.svg')

#Para evitar que se junten dos gráficas, ejecutamos otra vez:
plt.show()

#Ahora elegimos una variable(Edad) cuantitativa para crear un histograma
#Edad(x) y vemos cuanto se repite(y=frecuencia) para cada franja(step=5)
#Sabiendo que el MIN es 28 y MAX es 77(del Age.decribe anterior)...
#he decidido usar np.arange(25,85)
x=heart['Age']
plt.hist(x,edgecolor='black',bins=20)
plt.xticks(np.arange(25,85, step=5))
plt.title("Figura 1. Edades")
plt.ylabel('Frequency')
plt.xlabel('Age')
plt.axvline(x=m_age, linewidth=1, linestyle= 'solid', color="red", label='Mean')
plt.axvline(x=m_age-sd_age, linewidth=1, linestyle= 'dashed', color="green", label='- 1 S.D.')
plt.axvline(x=m_age + sd_age, linewidth=1, linestyle= 'dashed', color="green", label='+ 1 S.D.')

plt.savefig('Figure 1.svg')

#Para evitar que se junten dos gráficas, ejecutamos otra vez:
plt.show()

#Ahora elegimos una variable(Edad) cuantitativa para crear un histograma
#Edad(x) y vemos cuanto se repite(y=frecuencia) para cada franja(step=5)
#Sabiendo que el MIN es 28 y MAX es 77(del Age.decribe anterior)...
#he decidido usar np.arange(25,85)
x=heart['Cholesterol']
plt.hist(x,edgecolor='black',bins=20)
plt.xticks(np.arange(0,610, step=50))
plt.title("Figura 2. Colesterol")
plt.ylabel('Frequency')
plt.xlabel('Cholesterol level')
plt.axvline(x=m_cho, linewidth=1, linestyle= 'solid', color="red", label='Mean')
plt.axvline(x=m_cho-sd_cho, linewidth=1, linestyle= 'dashed', color="green", label='- 1 S.D.')
plt.axvline(x=m_cho + sd_cho, linewidth=1, linestyle= 'dashed', color="green", label='+ 1 S.D.')


plt.savefig('Figure 2.svg')
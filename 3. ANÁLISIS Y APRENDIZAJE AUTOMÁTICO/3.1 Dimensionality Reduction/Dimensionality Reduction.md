# Reducción de Dimensionalidad

La dimensionalidad es el número de características de un modelo.
La dimensionalidad es elevada cuando el número de características es mayor al número de observaciones N.

## Curso de dimensionalidad
- <strong>Dimensionalidad</strong>: El número de características de un modelo.
- <strong>High Dimensional Data</strong>: Cuando características p es > a N observaciones.

<strong>Si queremos realizar una clasificación, para crear un algoritmo:</strong>
1. En ML, tendemos a añadir el mayor número de características.
2. Conforme vamos añadiendo, hay un momento en el que el modelo empeora.
3. Tendencia al overfitting.

Entonces ¿cuántas características debe tener un modelo?
crear tabla mermaid

### Feature Selection y Feature Extraction

1. Selección de Variables (FS): seleccionar el conjunto óptimo de características relevantes.
2. Extracción de Variables (FE): crear un nuevo subconjunto más pequeño de características relevantes, manteniendo la mayor parte de la información.

### Dimensionality Reduction

Para conjuntos de datos de alta dimensión (es decir, con número de dimensiones más de 10), reducción de la dimensión se realiza generalmente antes de la aplicación de un K-vecinos más cercanos (k-NN) con el fin de evitar los efectos de [la maldición de la dimensionalidad](https://es.wikipedia.org/wiki/Maldici%C3%B3n_de_la_dimensi%C3%B3n). 

La extracción de características y la reducción de la dimensión se puede combinar en un solo paso utilizando análisis de componentes principales ([PCA](https://es.wikipedia.org/wiki/An%C3%A1lisis_de_componentes_principales)), análisis discriminante lineal (LDA), o análisis de la correlación canónica (CCA) técnicas como un paso pre-procesamiento seguido por la agrupación de K-NN en vectores de características en el espacio reducido dimensión. En aprendizaje automático este proceso de pocas dimensiones también se llama incrustar.​

<strong>Ventajas de la reducción de dimensionalidad:
- Reduce el espacio de tiempo y almacenamiento requerido.
- La eliminación de multicolinealidad mejora el rendimiento del modelo de aprendizaje automático.
- Se hace más fácil de visualizar los datos cuando se reduce a dimensiones muy bajas tales como 2D o 3D.

También cabe mencionar la utilidad de la <strong>normalización</strong>:
El término unidad tipificada, variable centrada reducida, variable estandarizada o normalizada se utiliza en estadística para comparar datos procedentes de diferentes muestras o poblaciones.

## Filter Methods

Los métodos de filtrado evalúan la relevancia de los predictores fuera de los modelos de predicción y posteriormente modelan sólo los predictores que que superan algún criterio.

- Funcionan como parte del procesamiento de datos. La selección de variables es Independiente de los modelos de ML
- Clasifican las variables en función de la correlación que tienen con la variable de salida (Output).
- Se utilizan criterios univariados.

crear mermaid


¿Qué métodos existen?

crear mermaid

<strong> t-SNE </strong>

- Es una técnica para visualizar datos de alta dimensión con FE, mediante observaciones que son más diferentes en un espacio de altas dimensiones.
- Debido a esto, las observaciones que son similares estarán más cercanas entre si y pueden agruparse.
- No funciona con variables categóricas.
- Captura relaciones No lineales entre variables
Más información [aquí](https://datascientest.com/es/comprende-el-algoritmo-t-sne-en-3-pasos).

Otros métodos de filtro serían:
- ANOVA Test
- F-Test
- Spearman’ss
- Krusal-Wallis Test
- AUC Filter
- Relief Algorithm
- FCBF algorithm

<strong> ¿Qué métodos utilizar? </strong>

crear mermaid

<strong>Ventajas y desventajas de los métodos de filtro</strong>
crear mermaid


## Wrapping Methods

- Se utiliza un subconjunto de variables para determinar la capacidad predictiva
- Se añaden o eliminan características a este subconjunto.
- Se entrena el modelo
- Computacionalmente costosos.
- Se puede definir como un problema de búsqueda
1. <strong>Forward Selection (FS)</strong>:
Empieza con un conjunto vacío de características (Reduced Set). La mejor variable de las restantes se añade a este Reduced Set. En cada iteración posterior, la mejor de las variables sobrantes se añade a este subconjunto hasta que la adición de una nueva variable no mejore el rendimiento del modelo.

2. <strong>Backward Selection (BS)</strong>: Comienza con todas las variables e, iterativamente, se elimina la menos importante, lo cual va mejorando el modelo. El proceso se repite hasta que no hay mejora eliminando variables

3. <strong>Bidirectional Elimination</strong>: Es la combinación de los dos métodos anteriores (FS y BS). En cada una de las iteraciones el proceso selecciona el mejor de los atributos y elimina el peor de los restantes. El método termina cuando los dos métodos (FS y BS) encuentran el mismo subconjunto de variables.

4. <strong>Random Generation</strong>: Empieza con un subconjunto aleatorio de búsqueda de variables. Añadir o quitar un variable también se decide de forma aleatoria. A diferencia de FS o BE, el tamaño del subconjunto de características no puede ser determinado.

<strong>Ventajas y Desventajas de los métodos de Envoltorio (Wrapper) </strong>

crear mermaid


## Embeded Methods
- Combinan las cualidades métodos de filtro y los mérodos de Wrapper
- Las variables no son descartadas en estos métodos. Se utilizan como parámetros y se les da un peso muy bajo. Se conoce como Regularización
- Más rápidos de Entrenar

<strong>Intuición de la Regularización</strong>
- Overfitting ocurre cuando un modelo estadístico o de ML se adapta a un conjunto de datos pero es incapaz de gneralizar en otros conjuntos de datos.
- Suele suceder en modelos complejos como las Deep Neural Networks.
- Regularización es un proceso de introducir información adicional para evitar el overfitting.
- Existen numerosas regularizaciones, aunque las más famosas son las de L1 (Lasso) y L2 (Rdige).

## Modelos basados en Árboles

- Random Forest son una combinación de árboles de decisión
- También podemos usar la combinación de Modelos con Feature Selecion
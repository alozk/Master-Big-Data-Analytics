**ETL**

Proceso en el cual las organizaciones mueven datos desde múltiples fuentes, se formatean, se limpian, se cargan a otra base de datos, data mart, o data warehouse para analizar u otros.

ETL vs ELT

Básicamente es:

Extract, Transform and Load vs Extract Load and Transform.

ETL = extraes datos, los transformas en una estructura compatible, y cargarlo en un objetivo de datos sistema de almacén, por lo que las herramientas de inteligencia empresarial puede consultarlo y analizarlo.

ELT = extrae los datos, cárguelos inmediatamente en el sistema de lago de datos de destino y, a continuación, transforme el dato, por lo que las herramientas de inteligencia empresarial pueden consultar y analizarlo ELT generalmente se refiere a los datos proceso de transformación necesario para transformar los datos ya se encuentra en un lago de datos o almacén.

STAGING

![Graphical user interface

Description automatically generated](Aspose.Words.d5e91d03-827e-41fb-91c8-541f2e1b0ec6.001.png)Proceso imprescindible en una ETL






ETL

E de Extracción

En este paso, los datos se extraen del sistema de origen en el área de staging. Las transformaciones, si las hay, se realizan en el área de staging para que el rendimiento del sistema de origen no se degrade.

Modos de extracción

Básicamente, existen tres modos distintos de extracción. El tipo de necesidad de la organización es lo que, normalmente, determinará la elección de una u otra forma.

Full Extract o extracción total

Esta modalidad consiste en extraer la totalidad de datos. En este caso, se barren tablas completas que pueden llegar a tener millones de registros.

Incremental Extract o extracción incremental

Se va procesando por lotes únicamente lo que fue modificado o agregado. También puede haber filas que se borren por estar duplicadas, tratarse de datos erróneos, etc.

Update Notification o notificación de actualizaciones

En este caso, solo se van extrayendo los datos a medida que se produce una actualización (por ejemplo, un inserto). Estos tres tipos de extracción son manejados por un módulo denominado Change Data Capture (CDC).

ETL

T de Transformación

La fase de transformación de un proceso de ETL aplica una serie de reglas de negocio o funciones sobre los datos extraídos para convertirlos en datos que serán cargados. Estas directrices pueden ser declarativas, pueden basarse en excepciones o restricciones, pero, para potenciar su pragmatismo y eficacia, hay que asegurarse de que sean:

▪ Declarativas.

▪ Independientes.

▪ Claras.

▪ Inteligibles.

▪ Con una finalidad útil para el negocio.

ETL

L de Load

La fase de carga es el momento en el cual los datos de la fase anterior (transformación) son cargados en el sistema de destino.

•Acumulación simple: La acumulación simple es la más sencilla y común, y consiste en realizar un resumen de todas las transacciones comprendidas en el período de tiempo seleccionado y transportar el resultado como una única transacción hacia el data warehouse, almacenando un valor calculado que consistirá típicamente en un sumatorio o un promedio de la magnitud considerada.

•Rolling: El proceso de Rolling por su parte, se aplica en los casos en que se opta por mantener varios niveles de granularidad. Para ello se almacena información resumida a distintos niveles, correspondientes a distintas agrupaciones de la unidad de tiempo o diferentes niveles jerárquicos en alguna o varias de las dimensiones de la magnitud almacenada (por ejemplo, totales diarios, totales semanales, totales mensuales, etc.).



![Graphical user interface

Description automatically generated](Aspose.Words.d5e91d03-827e-41fb-91c8-541f2e1b0ec6.002.png)





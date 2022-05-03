# DATA GOVERNANCE

1. Data Strategy

Es una nueva forma de gestionar estratégicamente los datos para alcanzar ventajas analíticas y conseguir nuestros objetivos de crecimiento.

Tenemos la necesidad de analizar que esperamos de un data strategy.

Estos son los requerimientos/pilares:

- Los datos pueden ser encontrados fácilmente.
- Los datos tienen que ser comprendidos con facilidad.
- Los datos son correctos.
- Los datos están completos
- Los datos son consistentes en el tiempo.
- Los datos necesitan ser trazados.

Hacia arquitecturas centradas en datos

Los problemas de análisis y presentación de informes se relacionan más a menudo con

problemas de gobierno de datos, no problemas de tecnología.

A medida que las organizaciones avanzan hacia un entorno data-centric world, el gobierno de datos se vuelve más crítico para asegurar que los datos sean consistentes, confiables y utilizables para analizar.

Un data strategy ayuda asegurando que los datos son gestionados y utilizados como un activo.

<p align="center">
Cambio de mentalidad cultural</p>

```mermaid
flowchart TB
subgraph "'Data is a part of your business, not a tool for it'"
a(((Define))) ==== b(((Align)));
b(((Align))) ==== c(((Manage)));
end
```
```mermaid
flowchart LR
d(Measure and Monitor) ---- e(Apply)
e(Apply) ---- f(Define)
f(Define) <---->g(Discover)
g(Discover) --- d(Measure and Monitor)
```

<p align="center">
Business e IT, objetivos comunes</p>

```mermaid
flowchart LR
a(Data) --- |Mantain| b(IT)
b(IT) --- |Support| c(Business)
c(Business) --- |Use| a(Data)
```

#

2. Roles y Responsabilidades
</p>

```mermaid
flowchart LR
A(Data Consumer) === B(Content Owner) === C(Platform Owner) === D(Data Steward)
```

#

3. Modelo de datos
- Físico

Define los componentes y servicios de bases de datos lógicas que se requieren para construir un database o diseño de una ya existente.

Un modelo físico de datos consiste en la estructura de la tabla, los nombres de las columnas y valores, claves foráneas y primarias y la relaciones entre las tablas.

- Lógico

Describe los datos con el mayor detalle posible, independientemente a cómo serán los físicos implementados en la database. Características de un modelo de datos lógicos incluye: todas las entidades y relaciones entre ellas. Todos los atributos para cada entidad son especificados.

- Conceptual

Es una vista empresarial estructurada de los datos necesarios para dar soporte a los procesos del negocio, registrar eventos comerciales y

seguimiento de las medidas de rendimiento relacionadas.

Se centra en la identificación de los datos utilizados en el negocio, pero no en su procesamiento flujo o características físicas.

<p align="center">
Tooling election</p>

```mermaid
flowchart TB
A[Tooling Election] ===> B([Data Catalogue])
A[Tooling Election] ===> C([Data Governance])
A[Tooling Election] ===> D([Data Quality])
```

#

4. Comités y funcionamiento
<p align="center">

```mermaid
flowchart TB
A[Data Governance Operating Model] == Establishes & Drives ==> B[Data Stewardship Activities]
B[Data Stewardship Activities] == Reports & Escalates ==> A[Data Governance Operating Model]
B[Data Stewardship Activities] == Aligns & Coordinates ==> C[IT/Operational Data Management Activities]
C[IT/Operational Data Management Activities] == Monitors & Remediates ==> B[Data Stewardship Activities]
```


<p align="center">
Real scenarios</p>

```mermaid
stateDiagram-v2
s1 : Scenario 1
s2 : Scenario 2
s3 : Scenario 3
s4 : Scenario 4
NE : New Entity
NA : New Attribute
QI : Quality Issue
NR : New Report
s1 --> NE
s2 --> NA
s3 --> QI
s4 --> NR
```

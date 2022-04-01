**UNIX**

**¿QUÉ ES?**

Hoy en día los sistemas operativos Unix son ampliamente utilizados en multitud de dispositivos que abarcan desde los supercomputadores más capaces hasta los teléfonos móviles más populares, pasando por los ordenadores que utilizamos diariamente en nuestros escritorios. La filosofía de los sistemas Unix se caracteriza por:

- Un sistema de ficheros jerárquico,
- Una gran colección de pequeños programas que pueden trabajar en serie,
- El uso de ficheros de texto para almacenar los datos,

Tratar los dispositivos como ficheros.

**¿Practicamos?**

https://bellard.org/jslinux/

**Veamos que comandos son los más utilizados:**

![Pantalla de computadora con números](https://github.com/alozk/Master-Big-Data-Analytics/blob/main/FUNDAMENTOS/1.%20FUNDAMENTOS/2.%20LINUX%20%26%20UNIX/PICS/Aspose.Words.39bc4030-e64e-421a-baba-45acd83df99c.001.png)

**FICHEROS**

![Forma](https://github.com/alozk/Master-Big-Data-Analytics/blob/main/FUNDAMENTOS/1.%20FUNDAMENTOS/2.%20LINUX%20%26%20UNIX/PICS/Aspose.Words.39bc4030-e64e-421a-baba-45acd83df99c.002.png)


- **Directorio raíz (/)**

Todo archivo y directorio depende de un único **directorio raíz** o *root*, el cual se representa por el símbolo **/**. Si se dispone de varios dispositivos físicos de almacenamiento secundario, todos deben depender del directorio raíz, y el usuario tratará cada uno de los discos como un subdirectorio que depende del *root*.

- **Directorio de conexión (~)**

Directorio creado al dar de alta un usuario. El propósito de este directorio es suministrar un punto en la jerarquía de directorios del sistema de archivos UNIX a partir del cual el usuario puede almacenar y estructurar sus propios archivos y directorios. Suele ser tomado como **directorio de trabajo** inicial cuando el usuario establece una sesión de trabajo. Se representa mediante el símbolo **~**.

- **Directorio de trabajo (.)**

En el que operamos en cada momento de la sesión. Se representa mediante un punto (**.**). 

**SISTEMA**

Permisos

![Linux / Unix](https://github.com/alozk/Master-Big-Data-Analytics/blob/main/FUNDAMENTOS/1.%20FUNDAMENTOS/2.%20LINUX%20%26%20UNIX/PICS/Aspose.Words.39bc4030-e64e-421a-baba-45acd83df99c.003.png)

![PRORED | Los permisos de UNIX, Linux y Mac OS](https://github.com/alozk/Master-Big-Data-Analytics/blob/main/FUNDAMENTOS/1.%20FUNDAMENTOS/2.%20LINUX%20%26%20UNIX/PICS/Aspose.Words.39bc4030-e64e-421a-baba-45acd83df99c.004.png)

Unix desde su origen ha sido un sistema multiusuario. Para conseguir que cada usuario pueda trabajar en sus archivos, pero que no pueda interferir accidental o deliberadamente con los archivos de otros usuarios se estableció desde el principio un sistema de permisos.



![Permissions](https://github.com/alozk/Master-Big-Data-Analytics/blob/main/FUNDAMENTOS/1.%20FUNDAMENTOS/2.%20LINUX%20%26%20UNIX/PICS/Aspose.Words.39bc4030-e64e-421a-baba-45acd83df99c.005.png)


Ejemplo 1

Supongamos que hay permiso a todo para todos, en ese caso tendríamos que sumar 1+21+22 tanto para owner, como para group, como para public. En este caso el permiso sería: rwxrwxrwx con valor de 777. Dado que la suma anterior da 7 y se aplica a owner-group-public.

Ejemplo 2

Supongamos que el owner, tiene permiso a todo; el grupo, para leer y escribir; y el público, solo permiso para su lectura. En ese caso: owner = 1+21+22; grupo=21+22; y public=22. Con lo cual el permiso sería: rwx-rw-r-- con valor de 764.

Practica y conoce mas posibilidades en el enlace: <https://chmod-calculator.com/>


Unidades de disco

Cada sistema puede tener una o mas particiones, las cuales son regiones de un medio de almacenamiento. En Windows suele haber una partición por disco mientras que no es tan común en Linux. En Unix la jerarquía cuelga de la raíz y en Windows cada partición tiene su propia jerarquía.

**SCRIPT**

Bash

Bourne-again Shell, es una popular [interfaz de usuario de línea de comandos](https://es.wikipedia.org/wiki/Interfaz_de_l%C3%ADnea_de_comandos "Interfaz de línea de comandos"), específicamente un [shell de Unix](https://es.wikipedia.org/wiki/Shell_de_Unix "Shell de Unix"); así como un [lenguaje de scripting](https://es.wikipedia.org/wiki/Script "Script").

Bash es un [intérprete de órdenes](https://es.wikipedia.org/wiki/Interfaz_de_l%C3%ADnea_de_comandos "Interfaz de línea de comandos") que generalmente se ejecuta en una [ventana de texto](https://es.wikipedia.org/wiki/Emulador_de_terminal "Emulador de terminal") donde el usuario escribe órdenes en modo texto. Bash también puede leer y ejecutar órdenes desde un archivo, llamado **script**.

Ejemplo script

#!/bin/bash

echo "hello world"

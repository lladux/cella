# Cella
Cella es un sistema web de almacenamiento pensado para un uso local algo similar a un NAS, con integrcaciones que permiten facilitar al usuario en traspaso de archivos y proximamente carpetas entre diferentes dispositivos, el sistema soporta la existencias de diferentes usarios, estos usuarios tendran sus archvos solo accesibles por ellos y no por otros usuarios. En otras palabras el almacenamiento de cada usuario es privado.
El sistema puede ser ejecutado 
## Instrucciones 
### 1.  Clonar el repositorio.

*Elija en qué carpeta quiere clonar el repositorio.*
```bash
git clone https://github.com/lladux/cella.git
```
<br>

### 2 Acceder a la carpeta**
```bash
cd cella
```

<br>

### 3. Crear el entorno virtual

*Dentro de la carpeta que clono cree el entorno virtual.*
 [En caso de error, consultar en la documentación oficial.](https://docs.python.org/3/library/venv.html)
```bash
python -m venv venv
```
*O puedes tener una versión diferente de Python que utilicé python3 para ejecutarse.*
```bash
python3 -m venv venv
```
<br>

### 4. Activación del entorno virtual

*En la misma carpeta ingresé el siguiente comando para activar el entorno virtual.*

`Linux/MacOs`
```bash
source venv/bin/activate
```
`windows`
```bash
.\venv\Scripts\activate
```

 [En caso de error, consultar en la documentación oficial.](https://docs.python.org/3/library/venv.html)
<br>

### 5. Instalar dependencias

*En la misma carpeta ingresé el siguiente comando para instalar las dependencias necesarias.*
```bash
pip install -r requerimientos.txt  
```
<br>

### 6. Iniciar cella.

Ejecutamos el servidor con el archivo cella.py, que permite agilizar y automatizar el sistema

```bash
python cella.py 
```
*O si utiliza python3*
```bash
python3 cella.py  
```
*En caso de error, abra un "issue" para su pronta corrección.*

<br>

### 7. Crear el usuario staff

Al iniciar el servidor, se mostrarán dos direcciones IP. Utilice la primera: esta será la dirección con la que podrá conectarse desde otros dispositivos.

Desde cualquier dispositivo, cree una cuenta de usuario. **El primer usuario** creado tendrá privilegios de administrador (**staff**) y podrá **aceptar o rechazar nuevos usuarios.**
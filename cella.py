import socket
import os
import sys
from io import open
import secrets

version='0.0.2'
error='Sucedio un error probablemente no estas en el entorno virtual o no tienes las dependencias'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cella.settings')

def obtenerIP():
    ip=None
    try:
        conexion = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        conexion.settimeout(0)
        conexion.connect(('8.8.8.8',1))
        ip=conexion.getsockname()[0]
    except:
        print('No cuentas con una red por lo cual no poderas conectarte desde otros dispositivos de tu red local :c')

    finally:
        conexion.close
    if ip != None:
        print(' ')
        print('Tu ip es:')
        print('http://'+ip+':8000')
        print(' ')

def migraciones():
    try:
        from django.core.management import execute_from_command_line

        sys.argv = ['manage.py', 'makemigrations']
        execute_from_command_line(sys.argv)

        sys.argv = ['manage.py', 'migrate']
        execute_from_command_line(sys.argv)
    except:
        print(error)


def generadorKey():
    cellakey=open('cellakey','w')
    cellakey.write(secrets.token_urlsafe(64))
    cellakey.close()

def generadorInfoCella():
    registro= open('cella.log','w')
    registro.write(version)
    registro.close()

def ValidacionesArchivos():
    lista=os.listdir()
    if 'cella.log' in lista:
        cellalog=open('cella.log','r')
        actulaVersion=cellalog.readlines()
        print(actulaVersion)
        cellalog.close()   
        if cellalog == [] or actulaVersion[0] != version:
            migraciones()
            generadorInfoCella()

    else:
        migraciones()
        generadorInfoCella()

    if 'cellakey' in lista:
        keys=open('cellakey','r')
        if keys.read() == '':
            generadorKey()
    else:
        generadorKey()

def main():
    ValidacionesArchivos()
    obtenerIP()
    try:
        from django.core.management import execute_from_command_line
        sys.argv = ['manage.py','runserver','0.0.0.0:8000']
        execute_from_command_line(sys.argv)
    except:
        print(error)
    
if __name__ == '__main__':
    main()


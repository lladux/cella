import socket
import os
import sys
from io import open
import secrets

version='0.1.1'
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
    cellakey=open('cellakey','x')
    cellakey.write(secrets.token_urlsafe(64))
    cellakey.close()

def generadorInfoCella():
    registro= open('cella.log','x')
    registro.write(version)
    registro.close()

def ValidacionesArchivos():
    if not os.path.exists(os.path.join(os.getcwd(),'cellakey')):
        generadorKey()

    if not os.path.exists(os.path.join(os.getcwd(),'cella.log')):
        generadorInfoCella()
        migraciones()
        return None
    
    currentVersion=open('cella.log','r+')
    reference=currentVersion.readlines()
    if reference==[]:
        currentVersion.write(version)
        currentVersion.close
        migraciones()
        return None

    if reference[0]==version:
        return None
    
    reference[0]=version
    currentVersion.writelines(reference)
    currentVersion.close()
    migraciones()
    


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


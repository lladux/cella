import os
import shutil
from django.http import FileResponse
from django.core.files.storage import FileSystemStorage

class DataManage:
    def __init__(self, request):
#Inicia la ruta
        ruta=os.getcwd()
        nruta=ruta[::-1]
        ruta=''
        bandera=False
        j=-1
        for i in nruta:            
            if bandera==False and(i == '/' or i =='\\'):
                bandera=True
            if bandera==True:
                ruta=ruta+i
            j=j-1
            
        ruta= ruta[::-1]
        carpMain= os.path.join(ruta,'cellaStorage')
        if (not os.path.exists(carpMain)):
            os.mkdir(carpMain)
# Verifica si la carpeta existe si no existe la crea
        user = os.path.join(carpMain,str(request.user) )   
        if (not os.path.exists(user)):
            os.makedirs(user)
        self.ruta = user




    def read(self, rutaAlt=None):
        direcs=[]
        archi=[]
        if(rutaAlt==None):
            for i in os.listdir(self.ruta) :
                if os.path.isdir(os.path.join(self.ruta, i)):
                    direcs.append(i)
                else: 
                    archi.append(i)
            informacion={'carpetas':direcs, 'archivos':archi}
            return informacion   
        else:
            if(rutaAlt[0]=='.' or rutaAlt[0]=='/' or rutaAlt.find('..')>1):
                error='Intento de vulnerar el sistema fallido ;)'
                for i in os.listdir(self.ruta) :
                    if os.path.isdir(os.path.join(self.ruta, i)):
                        direcs.append(i)
                    else: 
                        archi.append(i)
                    informacion={'carpetas':direcs, 'archivos':archi, 'error':error}
                return informacion    
            else:
                nuevaRuta=os.path.join(self.ruta ,rutaAlt)
                for i in os.listdir(nuevaRuta) :
                    if os.path.isdir(os.path.join(nuevaRuta, i)):
                        direcs.append(i)
                    else: 
                        archi.append(i)
                informacion={'carpetas':direcs, 'archivos':archi, "ruta": rutaAlt}
                return informacion 
        

    def download(self,archivo, ruta):
        rutaActual=os.path.join(self.ruta,ruta)
        rutaArchivo=os.path.join(rutaActual,archivo)
        file=open(rutaArchivo, 'rb')
        respuesta = FileResponse(file, as_attachment=True)
        return respuesta
    
    def downloadDir(self,nombre,ruta):
        rutaActual=os.path.join(self.ruta,ruta)
        rutaArchivo=os.path.join(rutaActual,archivo)
        Compresor = zipfile.ZipExtFile
        respuesta = FileResponse(rutaArchivo, as_attachment=True)
        return respuesta


    def backDir(self, ruta):
        nruta=ruta[::-1]
        ruta=''
        bandera=False
        j=-1
        for i in nruta:   
            if bandera==True:
                ruta=ruta+i         
            if bandera==False and(i == '/' or i =='\\'):
                bandera=True
            j=j-1         
        ruta= ruta[::-1]
        return ruta
    
    def delete(self, nombre, tipoArchivo, ruta='',):
        nruta = os.path.join(self.ruta, ruta)
        ruta= os.path.join(nruta, nombre)
        if tipoArchivo:
            os.remove(ruta)
        else:
            shutil.rmtree(ruta, ignore_errors=False)

    def createDirectory(self,nombre, ruta=''):  
        if(nombre=='..' or nombre=='.' or nombre.find('/')>=0 or nombre.find('\\')>=0):
            return'Ese tipo de carpetas no se permiten: '+ nombre
        rutaActual=os.path.join(self.ruta, ruta)
        archivo=os.path.join(rutaActual, nombre)
        if(os.path.exists(archivo)):
            return'La carpeta ya existe'
        else:
            os.makedirs(archivo)

    def rename(self, tipo, ruta, oldname, newname, extension=None):
        diferenteNombre=True
        rutaActual=os.path.join(self.ruta,ruta)
        if(oldname!=newname):
            if(tipo=='dir'):
                for i in os.listdir(rutaActual):
                    if(os.path.isdir(os.path.join(rutaActual,i)) and i==newname):
                        diferenteNombre=False
                        break
                if diferenteNombre:
                    newDir=os.path.join(rutaActual,newname)
                    oldDir=os.path.join(rutaActual,oldname)
                    os.rename(oldDir,newDir)
                else:
                    return "Tienes el mismo nombre en otra carpeta"
            else:
                for i in os.listdir(rutaActual):
                    if(i == newname and os.path.isdir(os.path.join(rutaActual,i))==False):
                        diferenteNombre=False
                        break
                if diferenteNombre:
                    if(extension=='on'):
                        if (oldname.find('.')==-1):
                            oldFile=os.path.join(rutaActual,oldname)
                            newFIle=os.path.join(rutaActual,newname)
                            os.rename(oldFile,newFIle)
                        else:
                            oldFile=os.path.join(rutaActual,oldname)
                            extensionName='.'+(oldname.split('.',1))[1]
                            newFIle=os.path.join(rutaActual,newname+extensionName)     
                            os.rename(oldFile,newFIle)
                    else:
                        oldFile=os.path.join(rutaActual,oldname)
                        newFIle=os.path.join(rutaActual,newname)
                        os.rename(oldFile,newFIle)
                else: 
                    return 'El archivo ya existe'
        else:
            return "Es el mismo nombre"


    def uploadFile(self, data, name, ruta, tipo):
        rutaActual= os.path.join(self.ruta, ruta)
        if (tipo=='file'):
            for i in os.listdir(rutaActual):
                if( i == name and os.path.isdir(os.path.join(rutaActual,i))==False):
                    return 'el archivo tiene el mismo nombre'
                    break
            fileSystemDj=FileSystemStorage(rutaActual)
            fileSystemDj.save(name,data)


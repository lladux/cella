import os
import shutil
from django.http import FileResponse, HttpResponse

from django.core.files.storage import FileSystemStorage
import zipfile

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
        if(rutaAlt==None or rutaAlt==''):
            for i in os.listdir(self.ruta) :
                if os.path.isdir(os.path.join(self.ruta, i)):
                    direcs.append(i)
                else: 
                    archi.append(i)
            informacion={'carpetas':direcs, 'archivos':archi}
            return informacion   
        else:
            if(rutaAlt[0]=='.' or rutaAlt[0]=='/' or rutaAlt.find('..')>=0):
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
        

    def download(self, fileCient, pathClient=''):
        CurrentPath=os.path.join(self.ruta, pathClient)
        pathfile=os.path.join(CurrentPath, fileCient)
        file=open(pathfile, 'rb')
        response = FileResponse(file, as_attachment=True)
        return response
    

    def downloadDir(self, pathDir, pathClient=''):
        try:
            response=HttpResponse(content_type='application/zip')

            with zipfile.ZipFile(response,'w', zipfile.ZIP_DEFLATED, False) as tmpZip:

                for rootPath, dirs, files in os.walk(os.path.join(self.ruta,pathDir )):
                    for fileName in files:
                        tmpZip.write(os.path.join(rootPath, fileName), os.path.relpath(os.path.join(rootPath, fileName),os.path.join(self.ruta,pathDir)))
                response['Content-Disposition'] = 'attachment; filename={}'.format(pathDir)

                return response
        except:
            return {'error':"Por el momento solo podemos realizar zips de maximo 2GB"}


    def backDir(self, path):
        reversePath=path[::-1]
        path=''
        flag=False
        for i in reversePath:   
            if flag==True:
                path=path+i         
            if flag==False and(i == '/' or i =='\\'):
                flag=True
        path= path[::-1]
        return path
    

    def delete(self, nombre, tipoArchivo, ruta='',):
        nruta = os.path.join(self.ruta, ruta)
        ruta= os.path.join(nruta, nombre)
        if tipoArchivo:
            os.remove(ruta)
        else:
            shutil.rmtree(ruta, ignore_errors=False)


    def createDirectory(self,nombre, ruta=''):  
        if(nombre.find('..')>=0 or nombre=='.' or nombre.find('/')>=0 or nombre.find('\\')>=0):
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
        if(newname.find('..')>=0 or newname=='.' or newname.find('/')>=0 or newname.find('\\')>=0):
            return'Ese tipo de nombre no se permiten: '+ newname
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
        newUserPath= os.path.join(self.ruta, ruta)
        if (tipo=='file'):
            for i in os.listdir(newUserPath):
                if( i == name and os.path.isdir(os.path.join(newUserPath,i))==False):
                    return 'el archivo tiene el mismo nombre'
                    break
            fileSystemDj=FileSystemStorage(newUserPath)
            fileSystemDj.save(name,data)


# Esta funcion solo funiona en windows y linux porque usa / tengo que ver como validar si es / o \
    def uploadDir(self, data,dataName, ruta=None):
        if (ruta==None):
            ruta=''
        newUserPath=os.path.join(self.ruta, ruta)
        dataList=dataName.split('|')
        dataList.pop()
        nameDirMother=dataList[0].split('/',1)[0]
        for i in os.listdir(newUserPath):
                if( i == nameDirMother and os.path.isdir(os.path.join(newUserPath,i))):
                    return 'existe una carpeta con el mismo nombre'
                    break
        datalist=0
        for filename in dataList:
            PathsFile=filename.split('/')
            relativefilePath=newUserPath
            for numpath in range(filename.count("/")):
                IsPathExist=False
                for i in os.listdir(relativefilePath):
                    if( i == PathsFile[numpath] and os.path.isdir(os.path.join(relativefilePath,i))):
                        relativefilePath= os.path.join(relativefilePath,PathsFile[numpath])
                        IsPathExist=True
                        break
                if (not IsPathExist):
                    relativefilePath= os.path.join(relativefilePath,PathsFile[numpath])
                    os.makedirs(relativefilePath)
            fileSystemDj=FileSystemStorage(relativefilePath)
            fileSystemDj.save(PathsFile[filename.count("/")],data[datalist])
            datalist=datalist+1
            

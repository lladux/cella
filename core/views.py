from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from .mangeFiles import DataManage
from django.http import HttpResponse
from django.contrib.auth.models import User


import os

def index(request):    
    if (request.user.is_authenticated):
        info=DataManage(request)
        if(request.method=='POST'):

            if request.POST.get('fileDown'):
                ruta=request.POST.get('root')                    
                return  info.download(request.POST['fileDown'],ruta)
            
            elif request.POST.get('dirDown'):
                ruta=request.POST.get('root')      
                return  info.downloadDir(request.POST['dirDown'],ruta)
            
            elif(request.POST.get('dir')):
                if(request.POST.get('root')==None):
                    context=info.read(request.POST['dir'])
                    return render(request, 'index.html',context)
                else:
                    ruta=os.path.join(request.POST.get('root'),request.POST.get('dir'))
                    context=info.read(ruta)
                    return render(request, 'index.html',context)

            elif(request.POST.get('back')):
                rutaNueva=info.backDir(request.POST['back'])
                context=info.read(rutaNueva)
                return render(request, 'index.html',context) 
               
            elif(request.POST.get('del')):
                nombre=request.POST.get('del')
                tipo=(request.POST.get('type')=='file')
                if(request.POST.get('root')!=None):
                    ruta=request.POST.get('root')                    
                    info.delete(nombre, tipo, ruta)
                    context=info.read(ruta)
                    return render(request, 'index.html',context)
                else:
                    info.delete(nombre, tipo)
                    context=info.read()
                    return render(request, 'index.html',context)
                
            elif(request.POST.get('nameDir')):
                name=request.POST.get('nameDir')
                ruta=request.POST.get('DirDelRoot')
                validacion=info.createDirectory(name,ruta)    
                context=info.read(ruta)
                if(validacion!=None): context['error']=validacion
                return render(request, 'index.html',context)   
            
            elif(request.POST.get('oldName')):
                oldname=request.POST.get('oldName')
                newName=request.POST.get('NewName')
                ruta=request.POST.get('root')
                typeContext=request.POST.get('type')
                extension=request.POST.get('extension')
                validacion=info.rename(typeContext,ruta,oldname,newName,extension)
                context=info.read(ruta)
                if(validacion!=None): context['error']=validacion
                return render(request, 'index.html', context)
            
            elif(request.FILES.get('fileUp')):
                file=request.FILES['fileUp']
                name=file.name
                ruta=request.POST.get('root')
                info.uploadFile(file,name, ruta,'file')
                context=info.read(ruta)
                return render(request,'index.html', context)

            elif(request.FILES.get('dirUp')):
                data=request.FILES.getlist('dirUp')
                dataName=request.POST.get('listaArchvios')
                ruta=request.POST.get('root')
                validacion=info.uploadDir(data,dataName)
                context=info.read(ruta)
                if(validacion!=None): context['error']=validacion
                return render(request,'index.html',context)
    
                
            else:
                context=info.read()
                return render(request, 'index.html',context)   
            
        else:
            context=info.read()
            return render(request, 'index.html',context)
            
    else:
        return redirect('/login')
    


# secion    
class InicioSecion(generic.View):
    tamplate_name='login.html'
    user=''
    contra=''
    def get(self, request):
        if (request.user.is_authenticated):
            return redirect('/')
        return render(request, self.tamplate_name)
    def post(self, request):
        if (request.method == "POST"):
            self.user=request.POST['username']
            self.contra=request.POST['password']
            check=authenticate(request, username=self.user, password=self.contra)
            if check is not None:
                login(request, check)
                return redirect('/') 
            else:
                return render(request, self.tamplate_name)

def cierre(request):
    logout(request)
    return redirect('/login')

class Registro(generic.View):
    template_name='registro.html'
    def get(self, request):
        if (request.user.is_authenticated):
            return redirect('/')
        return render(request, self.template_name)
    def post(self, request):
        pass

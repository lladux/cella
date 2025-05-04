from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .models import PendingUsers

class PendingRequest:
    def savePandingUser(username, password1,password2 ,email):
        if (password1 != password2):
            return {'error':'No ccoinside la contrseña'} 
        if (not PendingUsers.objects.filter(UserName=username).exists() and not User.objects.filter(username=username).exists()):
            hashPassword=make_password(password1)
            pendingUser=PendingUsers(UserName=username, password=hashPassword, mail=email)
            pendingUser.save()
            return {'error':'La solicitud para ser parte fue enviada correctamente, se le notificara por parte del administrador si fue aceptado'} 
        else:
            return {'error':'el nombre ya existe'} 

        
    
    def acceptUser(name):
        if (PendingUsers.objects.filter(UserName=name).exists() and not User.objects.filter(username=name).exists()):
            userData=PendingUsers.objects.get(UserName=name)
            user = User(username=userData.UserName)
            user.password=userData.password
            user.email= userData.mail
            user.save()
            userData.delete()

    def refuseUser(name):
        if (PendingUsers.objects.filter(UserName=name).exists() and not User.objects.filter(username=name).exists()):
            userData=PendingUsers.objects.get(UserName=name)
            userData.delete()
        

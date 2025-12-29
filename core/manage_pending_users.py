from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .models import PendingUsers

class PendingRequest():
    def save_panding_user(username, password_1,password_2 ,email):
        if (password_1 != password_2):
            return {'error':'No coinside la contrseña'} 
        
        if (not PendingUsers.objects.filter(UserName=username).exists() and not User.objects.filter(username=username).exists()):
            hash_password = make_password(password_1)
            pending_user = PendingUsers(UserName=username, password=hash_password, mail=email)
            pending_user.save()
            return {'error':'La solicitud para ser parte fue enviada correctamente, se le notificara por parte del administrador si fue aceptado'} 
        else:
            return {'error':'el nombre ya existe'} 

    def accept_user(name):
        if (PendingUsers.objects.filter(UserName=name).exists() and not User.objects.filter(username=name).exists()):
            user_data = PendingUsers.objects.get(UserName=name)
            user = User(username=user_data.UserName)
            user.password = user_data.password
            user.email = user_data.mail
            user.save()
            user_data.delete()

    def refuse_user(name):
        if (PendingUsers.objects.filter(UserName=name).exists() and not User.objects.filter(username=name).exists()):
            user_data = PendingUsers.objects.get(UserName=name)
            user_data.delete()
        

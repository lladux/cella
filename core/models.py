from django.db import models

class PendingUsers(models.Model):
    UserName    = models.CharField(max_length=30,unique=True)
    password    = models.CharField(max_length=25)
    mail        = models.EmailField(max_length=254, blank=True)

    def __str__(self):
        return self.UserName

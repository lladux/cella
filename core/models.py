from django.db import models



class PendingUsers(models.Model):
    UserName    = models.CharField(max_length=30)
    password    = models.CharField(max_length=25)

    def __str__(self):
        return self.UserName

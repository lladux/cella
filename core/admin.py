from django.contrib import admin
from .models import PendingUsers
# Register your models here.

@admin.register(PendingUsers)
class PendingUsersAdmin(admin.ModelAdmin):
    list_display=[
        'UserName',
        'password',
        'mail'
    ]
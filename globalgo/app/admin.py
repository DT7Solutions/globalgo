from django.contrib import admin

from .models import *
# Register your models here.
class AdminUserlist(admin.ModelAdmin):
    list_display=('id','username','email')

class AdminRole(admin.ModelAdmin):
    list_display=('id','name')
    

admin.site.register(Users,AdminUserlist)
admin.site.register(Role,AdminRole)



# Register your models here.
from django.contrib import admin
from login.models import logindata

# Register your models here.
class loginAdmin(admin.ModelAdmin):
    list_display=('email','password')
admin.site.register(logindata,loginAdmin)
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from signup.models import signdata

# Register your models here.
class Modelssingups(admin.ModelAdmin):
    list_display=('user_name','email','password')
admin.site.register(signdata,Modelssingups)
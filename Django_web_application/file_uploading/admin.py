

# Register your models here.
from django.contrib import admin
from .models import img_uploader

# Register your models here.

class imguploaderAdmin(admin.ModelAdmin):
    list_display = ('imageFile',)

admin.site.register(img_uploader, imguploaderAdmin)

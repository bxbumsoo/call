from django.contrib import admin
from .models import Calloj

# Register your models here.


class Callmodel(admin.ModelAdmin):
    list_display = ['id', 'mdname', 'mdinfo']


admin.site.register(Calloj, Callmodel)

from django.contrib import admin
from .models import Get
from import_export.admin import ImportExportModelAdmin 

class BrandAdmin(ImportExportModelAdmin):
    pass

#Registeryourmodelshere.
admin.site.register(Get, BrandAdmin)
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from shiv.models import Contact,Wallq
# Register your models here.

admin.site.register(Contact,ImportExportModelAdmin)
admin.site.register(Wallq,ImportExportModelAdmin)
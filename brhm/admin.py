from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from brhm.models import Shabdkosh,Blogpage, Varnamala, Suktam , mantra, strotam, shlokas


# Register your models here.
admin.site.register(Shabdkosh,ImportExportModelAdmin)
admin.site.register(Varnamala,ImportExportModelAdmin)
admin.site.register(Blogpage,ImportExportModelAdmin)
admin.site.register(Suktam,ImportExportModelAdmin)
admin.site.register(mantra,ImportExportModelAdmin)
admin.site.register(strotam,ImportExportModelAdmin)
admin.site.register(shlokas,ImportExportModelAdmin)



# class ShabdkoshAdmin(ImportExportModelAdmin):
#     pass
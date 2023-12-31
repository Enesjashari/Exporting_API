from django.contrib import admin
from .models import *

# admin.site.register(Quote)



from import_export import resources
from import_export.admin import ImportExportModelAdmin

class StudentResource(resources.ModelResource):
    class Meta:
        model = Quote

class StudentAdmin(ImportExportModelAdmin):
    resource_class = StudentResource

admin.site.register(Quote,StudentAdmin)
admin.site.register(Contact)
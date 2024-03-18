from django.contrib import admin
from . import models
# Register your models here.
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('Name',)
admin.site.register(models.School, SchoolAdmin)
from django.contrib import admin
from crudapp import models
# Register your models here.

class listview(admin.ModelAdmin):
    list_display = ['name','section','address','phone']

admin.site.register(models.Students,listview)

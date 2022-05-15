from django.contrib import admin

# Register your models here.
from BackendRest import models
admin.site.register([models.Data])
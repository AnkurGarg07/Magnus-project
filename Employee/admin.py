from django.contrib import admin
from .models import employee

class employeeAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email','mobile','dob','Gender','address','country','city')

admin.site.register(employee,employeeAdmin)

# Register your models here.

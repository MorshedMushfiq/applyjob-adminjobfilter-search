from django.contrib import admin
from App.models import *

# Register your models here.

class CustomUserDisplay(admin.ModelAdmin):
    list_display = ['username', 'email', 'user_type']

admin.site.register(CustomUser,  CustomUserDisplay)

class JobDisplay(admin.ModelAdmin):
    list_display = ['job_title', 'company_name', 'user', 'location']
    
admin.site.register(JobModel, JobDisplay)

    




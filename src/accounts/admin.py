from django.contrib import admin

from .models import User

# Register your models here.


class UserModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_worker', 'is_recruiter', 'is_active', 'is_staff', 'date_joined']
    search_fields = ['username', 'email', 'is_worker', 'is_recruiter', 'is_active', 'is_staff', 'date_joined']


admin.site.register(User, UserModelAdmin)
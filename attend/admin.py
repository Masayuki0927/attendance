from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Attendance, CustomUser, Date

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('age',)}),)
    list_display = ['username', 'email', 'age']

admin.site.register(CustomUser, UserAdmin)

admin.site.register(Attendance)
admin.site.register(Date)
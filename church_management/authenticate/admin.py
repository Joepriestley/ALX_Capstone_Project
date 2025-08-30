from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.
class customAdminUser(UserAdmin):
    model =User
    list_display=["username","email", "phone_number","is_staff", "is_active","profile_img"]
    fieldsets =UserAdmin.fieldsets + (
        (None, {"fields":("phone_number","profile_img")}),
    )
    
    add_fieldsets =UserAdmin.add_fieldsets + (
        (None,{"fields": ("phone_number","profile_img")}),
    )
    
admin.site.register(User, customAdminUser)


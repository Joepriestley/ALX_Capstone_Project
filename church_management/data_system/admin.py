from django.contrib import admin
from .models import  Departement, Member,StatusHistory,Attendance
# Register your models here.

@admin.register(Departement)
class DepartementAdmin(admin.ModelAdmin):
    list_display =("name","leader")
    
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display=("first_name","middle_name","last_name","phone","country","address","date_joined","last_updated","status","departement","occupation",)
    search_fields=("first_name","last_name",)
    list_filter=("first_name","last_name",)
    ordering= ("last_name",)

@admin.register(StatusHistory)
class StatusHistoryAdmin(admin.ModelAdmin):
    list_display=("member","old_status","new_status","date_changed",)
    
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display=("member","event_date","event_type","status",)
    
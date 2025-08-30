from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from django_countries.serializers import CountryFieldMixin
from .models import Departement,Member,StatusHistory, Attendance
from authenticate.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=("id","username","phone_number","address","email")
        
class DepartementSerializer(serializers.ModelSerializer):
    class Meta:
        model= Departement
        fields ="__all__"
        
class StatusHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model= StatusHistory
        fields ="__all__"
        
class MemberSerializer(CountryFieldMixin,serializers.ModelSerializer):
    phone = PhoneNumberField()
    class Meta:
        model= Member
        fields ="__all__"
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields ="__all__"
        

from django.shortcuts import render
from rest_framework import viewsets
from .models import Departement, Attendance,Member,StatusHistory
from authenticate.models import  User
from .serializers import UserSerializer,DepartementSerializer,MemberSerializer,StatusHistorySerializer,AttendanceSerializer

# Create your views here.

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class MemberView(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    
class DepartementView(viewsets.ModelViewSet):
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer
    
class AttendanceView(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    
class StatusHistoryView(viewsets.ModelViewSet):
    queryset = StatusHistory.objects.all()
    serializer_class = StatusHistorySerializer

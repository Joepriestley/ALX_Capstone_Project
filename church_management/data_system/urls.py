from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MemberView,DepartementView, AttendanceView,StatusHistoryView,UserView

router =DefaultRouter()
router.register(r"members",MemberView)
router.register(r"departement",DepartementView)
router.register(r"attendance",AttendanceView)

urlpatterns =[
    path("", include(router.urls)),
]
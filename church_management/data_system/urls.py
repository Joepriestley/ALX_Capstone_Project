from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MemberView,DepartementView, AttendanceView,StatusHistoryView,UserView

router =DefaultRouter()
router.register(r"members", MemberView)
router.register(r"departement", DepartementView)
router.register(r"attendance", AttendanceView)
router.register(r"status-history",StatusHistoryView)

urlpatterns =[
    path("", include(router.urls)),
]
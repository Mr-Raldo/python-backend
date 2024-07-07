from django.urls import path
from .views import CompanyViewset, EmployeeViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("company", CompanyViewset, basename="company")
router.register("employee", EmployeeViewset, basename="employee")


urlpatterns = router.urls

# urlpatterns = [path("", home)]

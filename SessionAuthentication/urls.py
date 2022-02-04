from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

# Createing Router Object
router= DefaultRouter()

# Register EmployeeViewSet with Router
router.register('employeeapi',views.EmployeeModelViewSet,basename='employee')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework'))
]

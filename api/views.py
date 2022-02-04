from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly


# Model View Set 
class EmployeeModelViewSet(viewsets.ModelViewSet):
	queryset=Employee.objects.all()
	serializer_class=EmployeeSerializer
	authentication_classes=[SessionAuthentication]
	# permission_classes=[IsAuthenticated]
	# permission_classes=[AllowAny]
	# permission_classes=[IsAdminUser]
	# permission_classes=[IsAuthenticatedOrReadOnly]
	# permission_classes=[DjangoModelPermissions]
	permission_classes=[DjangoModelPermissionsOrAnonReadOnly]



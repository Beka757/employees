from django.urls import path
from api.views import (
    EmployeeListAPIView, RegistrationApiView, LogoutView,
    EmployeeApiCreateView, EmployeeApiUpdateView
)
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Employee API",
      default_version='v1',
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('schema/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('employee/', EmployeeListAPIView.as_view()),
    path('register/', RegistrationApiView.as_view(), name='registration'),
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('logout/', LogoutView.as_view(), name='api_token_auth'),
    path('employee/create/', EmployeeApiCreateView.as_view()),
    path('employee/<int:pk>/', EmployeeApiUpdateView.as_view())
]

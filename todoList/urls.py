from django.contrib import admin
from django.urls import path,include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

admin.site.site_header = 'Todo Admin'
admin.site.index_title = 'Admin'

# Schema view for API documentation
schema_view = get_schema_view(
    openapi.Info(
        title="todo API",
        default_version='v1.0.0',
        description="TOdo 🚀 Official API Documentation",
        terms_of_service="https://www.todo.com/terms",
        contact=openapi.Contact(email="tododev@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Define URL patterns for the project
urlpatterns = [
    # URL pattern for the ReDoc API documentation UI
    path('', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # URL pattern for the Django admin site
    path('admin/', admin.site.urls),
    # URL pattern for the Swagger API documentation UI
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # URL patterns for the API endpoints (version 1)
    path('api/v1/',include('api.urls')),
]

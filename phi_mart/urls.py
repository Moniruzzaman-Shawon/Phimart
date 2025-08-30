from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import api_root_view

# DRF-YASG Schema
schema_view = get_schema_view(
   openapi.Info(
      title="Phimart - E-commerce API",
      default_version='v1',
      description="API Documentation for Phimart E-commerce Project",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="m.zaman.djp@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_root_view),

    # app APIs
    path('api/v1/', include('api.urls'), name='api-root'),

    # Djoser auth endpoints (register, login, logout, password reset/change)
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),  # JWT auth

    # Swagger & Redoc documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# Debug Toolbar (only in development)
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns

# Static & Media files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

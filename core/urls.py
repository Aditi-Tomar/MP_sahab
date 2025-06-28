from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Swagger imports
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Voter Management API",
        default_version='v1',
        description="API documentation for Voter Management",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="your@email.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # API Endpoints (best practice: all at /api/<app>/)
    path('api/invitations/', include('invitations.api.urls')),
    path('api/blogs/', include('blogs.api.urls')),
    path('api/media_management/', include('Media_Management.api.urls')),
    path('api/passes/', include('passes.api.urls')),
    path('api/events/', include('events.api_urls', namespace='events_api')),
    path('api/news/', include('news.api.urls')),
   
    # REST Framework browsable API
    path('api-auth/', include('rest_framework.urls')),
    
    # Swagger/OpenAPI documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    # Web Views (non-API)
    path('', include('voters.urls')),
    path('events/', include('events.urls')),
    path('news/', include('news.urls')),
    path('notifications/', include('notifications.urls')),
    path('passes/', include('passes.urls')),
    path('media/', include('Media_Management.urls')),
    path('blogs/', include('blogs.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('invitations/', include('invitations.urls')),
]

# Customize admin site
admin.site.site_header = 'Voter Management System'
admin.site.site_title = 'Voter Management'
admin.site.index_title = 'Welcome to Voter Management System'

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#tocken- 6de781264d0c364047f200923f9d581996d5ac98
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Add only web views here if any
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
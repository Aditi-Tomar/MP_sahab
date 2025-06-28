from django.urls import path, include

urlpatterns = [
    path('', include('news.api.urls')),
]

from django.urls import path, include
from . import views

app_name = 'passes'

urlpatterns = [
    path('', views.pass_request_view, name='pass_request'),
    path('api/', include('passes.api.urls', namespace='pass_request')),

]
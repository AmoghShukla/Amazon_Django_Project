from django.urls import path
from AutoParts import views

urlpatterns = [
    path('', views.home, name='home'),
]
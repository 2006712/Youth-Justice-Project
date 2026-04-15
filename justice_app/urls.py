from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recommend/<int:youth_id>/', views.recommendations, name='recommendations'),
]

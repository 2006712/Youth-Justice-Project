from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.home, name='home'),

    # Recommendations page
    path('recommend/<int:youth_id>/', views.recommendations, name='recommendations'),
]
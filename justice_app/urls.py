from django.urls import path
from . import views

app_name = 'justice_app'

urlpatterns = [
    # Home
    path('', views.home, name='home'),

    # Youths
    path('youths/', views.youth_list, name='youth_list'),
    path('youths/add/', views.add_youth, name='add_youth'),

    # Offences
    path('offences/', views.offence_list, name='offence_list'),
    path('offences/add/', views.add_offence, name='add_offence'),

    # Support Programs
    path('programs/', views.support_program_list, name='support_program_list'),
    path('programs/add/', views.add_support_program, name='add_support_program'),

    # Recommendations
    path('recommend/<int:youth_id>/', views.recommendations, name='recommendations'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('youths/', views.youth_list, name='youth_list'),
    path('offences/', views.offence_list, name='offence_list'),
    path('programs/', views.support_program_list, name='support_program_list'),

    path('add-youth/', views.add_youth, name='add_youth'),
    path('add-offence/', views.add_offence, name='add_offence'),
    path('add-program/', views.add_support_program, name='add_support_program'),
]
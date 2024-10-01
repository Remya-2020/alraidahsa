from django.urls import path
from . import views


urlpatterns = [
path('',views.mhome,name='mhome'),
path('about',views.about,name='about'),
path('services',views.services,name='services'),
path('contactus',views.contactus,name='contactus'),

path('register', views.register, name='register'),

]
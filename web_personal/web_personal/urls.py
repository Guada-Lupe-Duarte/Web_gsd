from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('portafolio/', views.portafolio, name='portafolio'),
    path('contact/', views.contact, name='contact'),
    path('admin/', admin.site.urls),
]
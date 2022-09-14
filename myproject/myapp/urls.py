from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('services/', views.services, name = "services"),
    path('services/checklist', views.checklist, name ="checklist"),
    path('services/integration', views.data, name ="data"),
    path('services/dashboard', views.dashboard, name ="dashboard"),
    path('contact-us', views.contact, name="contact-us"),
    path('test/', views.test, name="test")
    
] 
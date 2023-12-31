"""
URL configuration for EasyDjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
import os
from .views import paypal_integration


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.portada, name='portada'),
    path('iniciar-sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('panel-de-control/', views.panel_de_control, name='panel_de_control'),
    path('paypal/', paypal_integration, name='paypal_integration'),
    path('men/', views.menu, name='menu'),
    ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) \
    + static(settings.TEMPLATES_URL, document_root = settings.TEMPLATES_ROOT)

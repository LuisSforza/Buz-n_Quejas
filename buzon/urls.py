"""buzon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from mensajes.views import lista_mensaje, nuevo_mensaje, actualizar_mensaje, borrar_mensaje

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',lista_mensaje, name='lista_mensajes'),
    path('nuevo/mensaje', nuevo_mensaje, name='nuevo_mensaje'),
    path('actualizar/mensaje/<int:pk>/', actualizar_mensaje, name='actualizar_mensaje'), #<int:pk> saber que tipo de dato que voy a poner en url
    path('borrar/mensaje/<int:pk>/', borrar_mensaje , name='borrar_mensaje'), #<int:pk> saber que tipo de dato que voy a poner en url

]

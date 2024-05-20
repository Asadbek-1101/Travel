"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from travel.views import home, about, reyslar, destination, country, batafsil, create_davlat, update_davlat, delete_davlat
from travel.views import batafsil2, xizmatlar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('xizmatlar/', xizmatlar, name="xizmatlar"),
    path('reyslar/', reyslar, name="reyslar"),
    #-------------------------------------------------------------
    path('country/<int:id>/', country, name="country"),
    path('destination/<int:id>/', destination, name="destination"),
    path('batafsil/<int:id>/', batafsil, name="batafsil"),
    path('batafsil2/<int:id>/', batafsil2, name="batafsil2"),
    # -------------------------------------------------------------
    path('create_davlat/', create_davlat, name="create_davlat"),
    path('update_davlat/<int:id>/', update_davlat, name="update_davlat"),
    path('delete_davlat/<int:id>/', delete_davlat, name="delete_davlat"),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

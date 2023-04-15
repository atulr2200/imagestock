"""imagestock URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.conf.urls.static import static
from django.contrib import admin
from .views import *
from signup.views import signaction
from login.views import loginaction



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', show_home_page),
    path('category/<int:cid>/', show_category_page),
    path('', home),
    path('search/',search),
    #path('sig/',dat_a),
    #path('imgview/', imgview),
    path('admin/', admin.site.urls),
    path('signup/',signaction),
    path('login/',loginaction),
    path('login/home', show_home_page),
  

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

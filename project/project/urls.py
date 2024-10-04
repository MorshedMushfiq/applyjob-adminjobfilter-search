"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from project.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginPage, name="loginPage"),
    path('logout/', logoutUser, name="logoutPage"),
    path('register/', register, name="register"),
    path('home/', home, name="home"),
    path('add_job/', addJob, name="add_job"),
    path('apply_now/<int:id>', applyNow, name="apply_now"),
    path('search/', searchJob, name="searchJob"),
    path('profile/', profile, name="profile"),
    path('createdJobsByAdmin/', createdJobsByAdmin, name="createdJobsByAdmin"),
    path('jobDelete/<int:id>', jobDelete, name='jobDelete'),
    path('jobEdit/<int:id>', jobEdit, name='jobEdit'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

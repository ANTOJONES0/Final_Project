"""
URL configuration for Architecture project.

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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home1,name='home1'),
    path('home1/',views.home1,name='home1'),
    path('home2/',views.home2,name='home2'),
    path('home3/',views.home3,name='home3'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('ourteam/',views.ourteam,name='ourteam'),
    path('pricingplan/',views.pricingplan,name='pricingplan'),
    path('service/',views.service,name='service'),
    path('project/',views.project,name='project'),
    path('blog1/',views.blog1,name='blog1'),
    path('blog2/',views.blog2,name='blog2'),
    path('contact/',views.contact,name='contact')

]

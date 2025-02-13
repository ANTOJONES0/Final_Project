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
    path('contact/',views.contact,name='contact'),
    path('Sustainable_Building/',views.sustainable,name='sustainable'),
    path('Renovation&Modeling/',views.renovation,name='renovation'),
    path('design&Planning/',views.design,name='design'),
    path('Project_Management/',views.projectm,name='projectm'),
    path('Custom_Construction/',views.custom,name='custom'),
    path('Furniture&Decor/',views.furniture,name='furniture'),
    path('blogdetails1/',views.blogdetails1,name='blogdetails1'),
    path('blogdetails2/',views.blogdetails2,name='blogdetails2'),
    path('blogdetails3/',views.blogdetails3,name='blogdetails3'),
    path('blogdetails4/',views.blogdetails4,name='blogdetails4'),
    path('blogdetails5/',views.blogdetails5,name='blogdetails5'),
    path('blogdetails6/',views.blogdetails6,name='blogdetails6'),
    path('blogdetails7/',views.blogdetails7,name='blogdetails7'),
    path('blogdetails8/',views.blogdetails8,name='blogdetails8'),
    path('blogdetails9/',views.blogdetails9,name='blogdetails9'),
    path('blogdetails10/',views.blogdetails10,name='blogdetails10'),
    path('blogdetails11/',views.blogdetails11,name='blogdetails11'),
    path('blogdetails12/',views.blogdetails12,name='blogdetails12'),
    path('house1/',views.house1,name='house1'),
    path('house2/',views.house2,name='house2'),
    path('house3/',views.house3,name='house3'),
    path('house4/',views.house4,name='house4'),
    path('house5/',views.house5,name='house5'),
    path('house6/',views.house6,name='house6'),
]

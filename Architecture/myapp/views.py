from django.shortcuts import render
from django.http import HttpResponse

def home1(request):
    return render(request,'home1.html')

def home2(request):
    return render(request,'home2.html')

def home3(request):
    return render(request,'home3.html')

def aboutus(request):
    return render(request,'aboutus.html')

def ourteam(request):
    return render(request,'ourteam.html')

def pricingplan(request):
    return render(request,'pricingplan.html')

def service(request):
    return render(request,'service.html')

def project(request):
    return render(request,'project.html')

def blog1(request):
    return render(request,'blog1.html')

def blog2(request):
    return render(request,'blog2.html')

def contact(request):
    return render(request,'contact.html')

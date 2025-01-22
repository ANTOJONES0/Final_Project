from django.shortcuts import render
from .models import Datas

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
    if request.method == 'POST':
        message = request.POST['message']
        company = request.POST['company']
        place = request.POST['place']
        email = request.POST['email']
        phone = request.POST['phone']

        obj = Datas()

        obj.Message = message
        obj.Company = company
        obj.Place = place
        obj.Email = email
        obj.Phone = phone

        obj.save()

    return render(request,'contact.html')

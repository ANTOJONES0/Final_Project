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

def sustainable(request):
    return render(request,'sustainable.html')
    
def renovation(request):
    return render(request,'renovation.html')

def design(request):
    return render(request,'designs.html')

def projectm(request):
    return render(request,'projectm.html')

def custom(request):
    return render(request,'custom.html')

def furniture(request):
    return render(request,'furniture.html')

def house1(request):
    return render(request,'house1.html')

def house2(request):
    return render(request,'house2.html')

def house3(request):
    return render(request,'house3.html')

def house4(request):
    return render(request,'house4.html')

def house5(request):
    return render(request,'house5.html')

def house6(request):
    return render(request,'house6.html')

def blogdetails1(request):
    return render(request,'blogdetails1.html')

def blogdetails2(request):
    return render(request,'blogdetails2.html')

def blogdetails3(request):
    return render(request,'blogdetails3.html')

def blogdetails4(request):
    return render(request,'blogdetails4.html')

def blogdetails5(request):
    return render(request,'blogdetails5.html')

def blogdetails6(request):
    return render(request,'blogdetails6.html')

def blogdetails7(request):
    return render(request,'blogdetails7.html')

def blogdetails8(request):
    return render(request,'blogdetails8.8html')

def blogdetails9(request):
    return render(request,'blogdetails9.html')

def blogdetails10(request):
    return render(request,'blogdetails10.html')

def blogdetails11(request):
    return render(request,'blogdetails11.html')

def blogdetails12(request):
    return render(request,'blogdetails12.html')

def contact(request):
    if request.method == 'POST':
        
        company = request.POST['company']
        place = request.POST['place']
        email = request.POST['email']
        phone = request.POST['phone']

        obj = Datas()

        
        obj.Company = company
        obj.Place = place
        obj.Email = email
        obj.Phone = phone

        obj.save()

    return render(request,'contact.html')

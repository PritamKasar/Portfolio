from django.shortcuts import render
from .models import Contacts
# Create your views here.
def Home(request):
    return render(request, 'Home.html')
def Contact(request):
    name  = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')
    contact_data = Contacts.objects.create(name=name, email=email, description=message)
    contact_data.save()
    return render(request, 'Home.html',{'success':'Form Submitted'})
def Project_QR_Attendance_Sys(request):
    return render(request,'Project_QR_Attendance_Sys.html')
def Project_QR_Vending_machine(request):
    return render(request,'Project_QR_Vending_machine.html')
from django.shortcuts import render
from django.http import HttpResponse
from vehicle.models import Customer
from vehicle.models import Staff, Stock

def index(request):
    context={ "total_stock":len(Stock.objects.all()) }
    return render(request , 'index.html', context)

def CustomerSignUp(request):
    if request.method == "POST":
        name = request.POST.get("Customer_name")
        Address = request.POST.get("Customer_address")
        PanCard = request.POST.get("Customer_PAN")
        AadharcardNo = request.POST.get("Customer_aadhar")
        PhoneNO = request.POST.get("Customer_phone")
        cus = Customer(CustomerName=name, CustomerAddress=Address, CustomerPanCard=PanCard, CustomerAadharcardNo=AadharcardNo, CustomerPhoneNo=PhoneNO)
        cus.save()
    return render(request, 'Customer.html')

def StaffSingUp(request):
    if request.method == "POST":
        Staffname = request.POST.get("Staff_name")
        Address = request.POST.get("Staff_address")
        PanCard = request.POST.get("Staff_PAN")
        AadharcardNo = request.POST.get("Staff_aadhar")
        PhoneNo = request.POST.get("Staff_phone")
        staff = Staff(Staffname=Staffname, Address=Address, PanCard=PanCard, AadharcardNo=AadharcardNo, PhoneNo=PhoneNo)
        staff.save()
    return render(request , 'Staff.html')

# Create your views here.

from django.shortcuts import render, redirect
from django.views import View
from .models import Customer, Driver, Remainder, Vehicle, Bookings
from django.http import HttpResponse

# For simplicity, using basic function-based views for form handling

def add_customer(request):
    if request.method == 'POST':
        CusName = request.POST.get('CusName')
        MobileNo = request.POST.get('MobileNo')
        Email = request.POST.get('Email')
        Address = request.POST.get('Address')
        Customer.objects.create(CusName=CusName, MobileNo=MobileNo, Email=Email, Address=Address)
        return redirect('customer_list')
    return render(request, 'adddriver.html')

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})

def add_driver(request):
    if request.method == 'POST':
        Name = request.POST.get('Name')
        MobileNo = request.POST.get('MobileNo')
        LicenseNo = request.POST.get('LicenseNo')
        LicenseExpDate = request.POST.get('LicenseExpDate')
        DateOfJoining = request.POST.get('DateOfJoining')
        TotalExperience = request.POST.get('TotalExperience')
        Address = request.POST.get('Address')
        Status = request.POST.get('Status')
        Driver.objects.create(Name=Name, MobileNo=MobileNo, LicenseNo=LicenseNo, LicenseExpDate=LicenseExpDate,
                              DateOfJoining=DateOfJoining, TotalExperience=TotalExperience, Address=Address, Status=Status)
        return redirect('driver_list')
    return render(request, 'addrem.html')

def driver_list(request):
    drivers = Driver.objects.all()
    return render(request, 'driver_list.html', {'drivers': drivers})

def add_remainder(request):
    if request.method == 'POST':
        VehicleID = request.POST.get('VehicleID')
        RemDate = request.POST.get('RemDate')
        Message = request.POST.get('Message')
        vehicle = Vehicle.objects.get(pk=VehicleID)
        Remainder.objects.create(VehicleID=vehicle, RemDate=RemDate, Message=Message)
        return redirect('remainder_list')
    vehicles = Vehicle.objects.all()
    return render(request, 'bookingrepot.html', {'vehicles': vehicles})

def remainder_list(request):
    remainders = Remainder.objects.all()
    return render(request, 'remainder_list.html', {'remainders': remainders})

def add_vehicle(request):
    if request.method == 'POST':
        VehicleRegNo = request.POST.get('VehicleRegNo')
        Name = request.POST.get('Name')
        Type = request.POST.get('Type')
        RegistrationExpDate = request.POST.get('RegistrationExpDate')
        VehicleGroup = request.POST.get('VehicleGroup')
        VehicleColour = request.POST.get('VehicleColour')
        Vehicle.objects.create(VehicleRegNo=VehicleRegNo, Name=Name, Type=Type, RegistrationExpDate=RegistrationExpDate,
                               VehicleGroup=VehicleGroup, VehicleColour=VehicleColour)
        return redirect('vehicle_list')
    return render(request, 'addnew.html')

def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicle_list.html', {'vehicles': vehicles})

def add_booking(request):
    if request.method == 'POST':
        CusID = request.POST.get('CusID')
        VehicleID = request.POST.get('VehicleID')
        DriverID = request.POST.get('DriverID')
        TripType = request.POST.get('TripType')
        StartLocation = request.POST.get('StartLocation')
        EndLocation = request.POST.get('EndLocation')
        ApproxKM = request.POST.get('ApproxKM')
        StartDate = request.POST.get('StartDate')
        EndDate = request.POST.get('EndDate')
        TotalAmount = request.POST.get('TotalAmount')
        Status = request.POST.get('Status')
        customer = Customer.objects.get(pk=CusID)
        vehicle = Vehicle.objects.get(pk=VehicleID)
        driver = Driver.objects.get(pk=DriverID)
        Bookings.objects.create(CusID=customer, VehicleID=vehicle, DriverID=driver, TripType=TripType,
                                StartLocation=StartLocation, EndLocation=EndLocation, ApproxKM=ApproxKM,
                                StartDate=StartDate, EndDate=EndDate, TotalAmount=TotalAmount, Status=Status)
        return redirect('booking_list')
    customers = Customer.objects.all()
    vehicles = Vehicle.objects.all()
    drivers = Driver.objects.all()
    return render(request, 'addcus.html', {'customers': customers, 'vehicles': vehicles, 'drivers': drivers})

def booking_list(request):
    bookings = Bookings.objects.all()
    return render(request, 'booking_list.html', {'bookings': bookings})

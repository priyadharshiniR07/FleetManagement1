from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from app.models import Customer, Driver, Remainder, Vehicle, Bookings

from django.db.models import Sum

def index(request):
    total_income = Bookings.objects.filter(Status='Active').aggregate(total=Sum('TotalAmount'))['total'] or 0
    total_expense = Bookings.objects.filter(Status='Inactive').aggregate(total=Sum('TotalAmount'))['total'] or 0
    context = {
        'total_income': total_income,
        'total_expense': total_expense,
    }
    return render(request,"index.html", context)

def addbook(request):
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
        return redirect('bookings')
    customers = Customer.objects.all()
    vehicles = Vehicle.objects.all()
    drivers = Driver.objects.all()
    return render(request, "addbook.html", {'customers': customers, 'vehicles': vehicles, 'drivers': drivers})

def addcus(request):
    if request.method == 'POST':
        CusName = request.POST.get('CusName')
        MobileNo = request.POST.get('MobileNo')
        Email = request.POST.get('Email')
        Address = request.POST.get('Address')
        Customer.objects.create(CusName=CusName, MobileNo=MobileNo, Email=Email, Address=Address)
        return redirect('cusinfo')
    return render(request, "addcus.html")

def adddriver(request):
    if request.method == 'POST':
        Name = request.POST.get('Name')
        MobileNo = request.POST.get('MobileNo')
        LicenseNo = request.POST.get('LicenseNo')
        LicenseExpDate = request.POST.get('LicenseExpDate')
        DateOfJoining = request.POST.get('DateOfJoining')
        TotalExperience = request.POST.get('TotalExperience')
        Address = request.POST.get('Address')
        Age = request.POST.get('Age')
        ReferenceNotes = request.POST.get('ReferenceNotes')
        Status = request.POST.get('Status')
        Driver.objects.create(Name=Name, MobileNo=MobileNo, LicenseNo=LicenseNo, LicenseExpDate=LicenseExpDate,
                              DateOfJoining=DateOfJoining, TotalExperience=TotalExperience, Address=Address, Age=Age,
                              ReferenceNotes=ReferenceNotes, Status=Status)
        return redirect('driverinfo')
    return render(request, "adddriver.html")

def addrem(request):
    if request.method == 'POST':
        VehicleID = request.POST.get('VehicleID')
        RemDate = request.POST.get('RemDate')
        Message = request.POST.get('Message')
        vehicle = Vehicle.objects.get(pk=VehicleID)
        Remainder.objects.create(VehicleID=vehicle, RemDate=RemDate, Message=Message)
        return redirect('remainder')
    vehicles = Vehicle.objects.all()
    return render(request, "addrem.html", {'vehicles': vehicles})

def addnew(request):
    if request.method == 'POST':
        VehicleRegNo = request.POST.get('VehicleRegNo')
        Name = request.POST.get('Name')
        Type = request.POST.get('Type')
        RegistrationExpDate = request.POST.get('RegistrationExpDate')
        VehicleGroup = request.POST.get('VehicleGroup')
        VehicleColour = request.POST.get('VehicleColour')
        apiUrl = request.POST.get('apiUrl')
        apiUsername = request.POST.get('apiUsername')
        apiPassword = request.POST.get('apiPassword')
        Vehicle.objects.create(VehicleRegNo=VehicleRegNo, Name=Name, Type=Type, RegistrationExpDate=RegistrationExpDate,
                               VehicleGroup=VehicleGroup, VehicleColour=VehicleColour, apiUrl=apiUrl,
                               apiUsername=apiUsername, apiPassword=apiPassword)
        return redirect('vehiclemag')
    return render(request, "addnew.html")

def basicinfo(request):
    vehicle = Vehicle.objects.first()
    return render(request, "basicinfo.html", {'vehicle': vehicle})

def bookingreport(request):
    return render(request,"bookingrepot.html")

def bookings(request):
    bookings = Bookings.objects.all()
    return render(request,"bookings.html", {'bookings': bookings})

def bookings2(request):
    bookings = Bookings.objects.all()
    return render(request, "bookings2.html", {'bookings': bookings})

def cusinfo(request):
    customers = Customer.objects.all()
    return render(request, "cusinfo.html", {'customers': customers})

def driverinfo(request):
    drivers = Driver.objects.all()
    return render(request, "driver_info.html", {'drivers': drivers})

def inex(request):
    return render(request,"in&ex.html")

def remainder(request):
    remainders = Remainder.objects.all()
    return render(request, "reminder.html", {'remainders': remainders})

def vehman(request):
    return render(request,"veh_man.html")

def vehicle(request):
    if request.method == 'POST':
        VehicleRegNo = request.POST.get('VehicleRegNo')
        Name = request.POST.get('Name')
        Type = request.POST.get('Type')
        RegistrationExpDate = request.POST.get('RegistrationExpDate')
        VehicleGroup = request.POST.get('VehicleGroup')
        VehicleColour = request.POST.get('VehicleColour')
        Vehicle.objects.create(VehicleRegNo=VehicleRegNo, Name=Name, Type=Type, RegistrationExpDate=RegistrationExpDate,
                               VehicleGroup=VehicleGroup, VehicleColour=VehicleColour)
        return redirect('vehiclemag')
    return render(request,"vehicle.html")

def vehiclemag(request):
    bookings = Bookings.objects.all()
    return render(request, "vehiclemag.html", {'bookings': bookings})

def map(request):
    return render(request,"map.html")

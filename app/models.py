from django.db import models

class Customer(models.Model):
    CusID = models.AutoField(primary_key=True)
    CusName = models.CharField(max_length=50)
    MobileNo = models.IntegerField()
    Email = models.CharField(max_length=50)
    Address = models.CharField(max_length=255)

    def __str__(self):
        return self.CusName

class Vehicle(models.Model):
    VehicleID = models.AutoField(primary_key=True)
    VehicleRegNo = models.IntegerField(unique=True)
    Name = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)
    RegistrationExpDate = models.DateField()
    VehicleGroup = models.CharField(max_length=255)
    VehicleColour = models.CharField(max_length=50)
    apiUrl = models.URLField(max_length=200, blank=True, null=True)
    apiUsername = models.CharField(max_length=100, blank=True, null=True)
    apiPassword = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.Name

class Driver(models.Model):
    DriverID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    MobileNo = models.IntegerField()
    LicenseNo = models.CharField(max_length=255)
    LicenseExpDate = models.DateField()
    DateOfJoining = models.DateField()
    TotalExperience = models.IntegerField()
    Address = models.CharField(max_length=255)
    Age = models.IntegerField(blank=True, null=True)
    ReferenceNotes = models.CharField(max_length=255, blank=True, null=True)
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]
    Status = models.CharField(max_length=8, choices=STATUS_CHOICES)

    def __str__(self):
        return self.Name

class Remainder(models.Model):
    RemainderID = models.AutoField(primary_key=True)
    VehicleID = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    RemDate = models.DateField()
    Message = models.CharField(max_length=255)

    def __str__(self):
        return f"Remainder {self.RemainderID} for Vehicle {self.VehicleID}"

class Bookings(models.Model):
    BookId = models.AutoField(primary_key=True)
    CusID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    VehicleID = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    DriverID = models.ForeignKey(Driver, on_delete=models.CASCADE)
    TripType = models.CharField(max_length=255)
    StartLocation = models.CharField(max_length=255)
    EndLocation = models.CharField(max_length=255)
    ApproxKM = models.IntegerField()
    StartDate = models.DateField()
    EndDate = models.DateField()
    TotalAmount = models.IntegerField()
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]
    Status = models.CharField(max_length=8, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Booking {self.BookId} for Customer {self.CusID}"

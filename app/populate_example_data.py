import os
import django
import sys

# Set up Django environment for standalone script
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

from app.models import Customer, Driver, Remainder, Vehicle, Bookings
from datetime import date

# Clear existing data
Customer.objects.all().delete()
Driver.objects.all().delete()
Remainder.objects.all().delete()
Vehicle.objects.all().delete()
Bookings.objects.all().delete()

# Create sample customers
customer1 = Customer.objects.create(CusName='John Doe', MobileNo=1234567890, Email='john@example.com', Address='123 Elm St')
customer2 = Customer.objects.create(CusName='Jane Smith', MobileNo=9876543210, Email='jane@example.com', Address='456 Oak St')

# Create sample vehicles
vehicle1 = Vehicle.objects.create(VehicleRegNo=1001, Name='Truck A', Type='Truck', RegistrationExpDate=date(2025,12,31), VehicleGroup='Group 1', VehicleColour='Red')
vehicle2 = Vehicle.objects.create(VehicleRegNo=1002, Name='Van B', Type='Van', RegistrationExpDate=date(2026,6,30), VehicleGroup='Group 2', VehicleColour='Blue')

# Create sample drivers
driver1 = Driver.objects.create(Name='Mike Johnson', MobileNo=5551234567, LicenseNo='L12345', LicenseExpDate=date(2024,11,30), DateOfJoining=date(2020,1,15), TotalExperience=5, Address='789 Pine St', Status='Active')
driver2 = Driver.objects.create(Name='Sara Lee', MobileNo=5559876543, LicenseNo='L67890', LicenseExpDate=date(2025,5,15), DateOfJoining=date(2019,3,10), TotalExperience=6, Address='321 Maple St', Status='Active')

# Create sample remainders
Remainder.objects.create(VehicleID=vehicle1, RemDate=date(2025,5,20), Message='Oil change due')
Remainder.objects.create(VehicleID=vehicle2, RemDate=date(2025,6,15), Message='Tire rotation due')

# Create sample bookings
Bookings.objects.create(CusID=customer1, VehicleID=vehicle1, DriverID=driver1, TripType='One-way', StartLocation='City A', EndLocation='City B', ApproxKM=100, StartDate=date(2025,5,1), EndDate=date(2025,5,2), TotalAmount=500, Status='Active')
Bookings.objects.create(CusID=customer2, VehicleID=vehicle2, DriverID=driver2, TripType='Round-trip', StartLocation='City C', EndLocation='City D', ApproxKM=200, StartDate=date(2025,5,3), EndDate=date(2025,5,5), TotalAmount=1000, Status='Active')

print("Sample data populated successfully.")

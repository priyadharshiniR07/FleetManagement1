from django.urls import path
from . import views

urlpatterns=[

    path("",views.index,name="index"),
    path("addbook/",views.addbook,name="addbook"),
    path("addcus/",views.addcus,name="addcus"),
    path("adddriver/",views.adddriver,name="adddriver"),
    path("addnew/",views.addnew,name="addnew"),
    path("addrem/",views.addrem,name="addrem"),
    path("basicinfo/",views.basicinfo,name="basicinfo"),
    path("bookingreport/",views.bookingreport,name="bookingreport"),
    path("bookings/",views.bookings,name="bookings"),
    path("bookings2/",views.bookings2,name="bookings2"),
    path("cusinfo/",views.cusinfo,name="cusinfo"),
    path("driverinfo/",views.driverinfo,name="driverinfo"),
    path("inex/",views.inex,name="inex"),
    path("remainder/",views.remainder,name="remainder"),
    path("vehman/",views.vehman,name="vehman"),
    path("vehicle/",views.vehicle,name="vehicle"),
    path("vehiclemag/",views.vehiclemag,name="vehiclemag"),
    path("map/",views.map,name="map")

]

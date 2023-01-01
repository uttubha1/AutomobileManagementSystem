from django.db import models


class Staff(models.Model):
    Staffname = models.CharField(max_length=20)
    Staffid = models.IntegerField(primary_key=True)
    Address = models.CharField(max_length=20)
    PanCard = models.CharField(max_length=20)
    AadharcardNo = models.CharField(max_length=20)
    PhoneNo = models.IntegerField()

class Vehicle(models.Model):
    VehicleType = models.CharField(max_length=20)
    VehicleNo =models.IntegerField(primary_key=True)
    Company = models.CharField(max_length=20)

class Stock(models.Model):
    Stock = models.IntegerField()
    VehicleNo = models.ForeignKey( Vehicle , on_delete=models.CASCADE)
    Stockid = models.IntegerField(primary_key=True)

class Bookingbystaff(models.Model):
    Bookingid = models.IntegerField(primary_key=True)
    Stockid = models.ForeignKey(Stock , on_delete=models.CASCADE)
    Staffid = models.ForeignKey(Staff, on_delete=models.CASCADE)

class Customer(models.Model):
    CustomerName = models.CharField(max_length=20)
    CustomerID = models.IntegerField(primary_key=True)
    CustomerAddress = models.CharField(max_length=20)
    CustomerPanCard = models.CharField(max_length=20)
    CustomerAadharcardNo = models.CharField(max_length=20)
    CustomerPhoneNo = models.IntegerField()

class Bookingbycustomer(models.Model):
    custid = models.IntegerField(primary_key=True)
    Stockid = models.ForeignKey(Stock, on_delete=models.CASCADE)
    Staffid = models.ForeignKey(Staff, on_delete=models.CASCADE)


# Create your models here.

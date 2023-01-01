from django.contrib import admin
from . models import Staff, Vehicle, Stock, Customer

admin.site.register(Customer)
admin.site.register(Staff)
admin.site.register(Vehicle)
admin.site.register(Stock)


# Register your models here.

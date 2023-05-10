from django.db import models

# Create your models here.
class customer(models.Model):
    name=models.CharField(max_length=250)
    phoneno=models.IntegerField(null=True)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    cnfrmpswd=models.CharField(max_length=50)






class twowheeler(models.Model):
   STATUS = (
       ('available', ('Available to borrow')),
       ('borrowed', ('Borrowed by someone')),
       ('archived', ('Archived - not available anymore')),
   )
   vehicle_name=models.CharField(max_length=25)
   vehicle_no=models.CharField(max_length=25)
   vehicleimage=models.ImageField(verbose_name='Image Thumb',upload_to='vehicle')
   rentalprice=models.IntegerField()
   milage=models.CharField(max_length=25)
   status = models.CharField(
       max_length=32,
       choices=STATUS,
       default='available',
   )

class contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    message=models.TextField()


class booking(models.Model):
    user=models.ForeignKey(customer,on_delete=models.CASCADE)
    vehicle=models.ForeignKey(twowheeler,on_delete=models.CASCADE)
    bookingdate=models.CharField(max_length=200)
    startdate=models.CharField(max_length=200)
    returndate=models.CharField(max_length=200)
    bookingpayment=models.IntegerField()

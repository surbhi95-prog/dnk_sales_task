# Create your models here.
from django.db import models
class Customerr(models.Model):

    class PaymentChoices(models.TextChoices):
        IMMEDIATE = "Immediate","Immediate"
        DAYS_7 = "7 Days" , "7 Days"
        DAYS_15 = "15 Days" , "15 Days"
        DAYS_30 = "30 Days" , "30 Days"
        DAYS_45 = "45 Days" , "45 Days"
        DAYS_60 = "60 Days" , "60 Days"
        DAYS_90 = "90 Days" , "90 Days"

    class StatusChoice(models.TextChoices):
        ACTIVE = "Active","Active"
        INACTIVE = "Inactive", "Inactive"

    class CustomerType(models.TextChoices):
        COMPANY = "Company","Company"
        INDIVIDUAL = "Individual" , "Individual"
        DISTRIBUTOR = "Distributor" ,"Distributor"
        DEALER = "Dealer" , "Dealer"
        CONTRACTOR = "Contractor", "Contractor"
        OTHER = "Other","Other"

    # choices_list = ['7 Days', '15 Days', '30 Days','45 Days', '60 Days', '90 Days']
    cust_code = models.CharField(max_length=20, unique=True)
    cust_name = models.CharField(max_length=100)
    cust_type = models.CharField(choices=CustomerType.choices)

    contact_person = models.CharField(max_length=100)
    email = models.EmailField(blank=True, default="")
    phone = models.CharField(max_length=10)
    address_line = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    gst_number = models.CharField(max_length=15,blank=True,default="")
    payment_terms = models.CharField(choices=PaymentChoices.choices)
    status = models.CharField(choices=StatusChoice.choices,default=StatusChoice.ACTIVE)
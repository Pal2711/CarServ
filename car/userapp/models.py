from django.db import models

# Create your models here.

class usersignup(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    username = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    password = models.CharField(max_length=25)
    
    def __str__(self):
        return self.username
    

class usercontact(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name  = models.TextField()
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name
    

class bookservice(models.Model):
    submited = models.DateTimeField(auto_now_add=True)
    name = models.TextField()
    phone = models.CharField(max_length=25)
    servicetype = [
        ("Diagnostic Test", "Diagnostic Test"),
        ("Engine Servicing", "Engine Servicing"),
        ("Tires Replacement", "Tires Replacement"),
        ("Oil Changing", "Oil Changing"),
        ("Car Wash", "Car Wash"),
        ("Battery Check", "Battery Check"),
        ("Brake Inspection", "Brake Inspection"),
        ("AC Service", "AC Service"),
    ]
    service = models.CharField(max_length=50, choices=servicetype)
    date = models.DateField()
    specialrequest = models.TextField()

    def __str__(self):
        return self.name
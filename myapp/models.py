from django.db import models

# Create your models here.
class Person(models.Model):
    GENDER_CHOICES = (

        ('MALE','Male🤦‍♂️🤦‍♂️'),
        ('FEMALE','Female🤦‍♀️🤦‍♀️'),
    )


    name = models.CharField(max_length=255,blank=False,null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15,null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    age = models.PositiveIntegerField(default=5)
    gender = models.CharField(max_length=20,choices=GENDER_CHOICES,null=True)
    def __str__(self):
        return f"{self.name} - {self.phone}"
    
class Mission(models.Model):
    name = models.CharField(max_length=255,blank=False,null=True)
    description = models.TextField(null=True,blank=True)
    photo   = models.ImageField(upload_to="mission",null=True)

    def __str__(self):
        return self.name


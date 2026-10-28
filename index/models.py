from django.db import models

# Create your models here.
class product(models.Model):
    title=models.CharField(max_length=100,blank=False,default='product1')
    image=models.ImageField(upload_to='image/',blank=False)
    name=models.CharField(max_length=100,blank=False)
    price=models.CharField(max_length=100,blank=False)

    def __str__(self):
        return self.name


class monthlydeal(models.Model):
    offer=models.CharField(max_length=100,blank=False)
    image=models.ImageField(upload_to='monthly_offer/',blank=False)
    name=models.CharField(max_length=100,blank=False)
    discription=models.TextField(max_length=300,blank=False)
    def __str__(self):
        return self.name


class logo(models.Model):
    title=models.CharField(max_length=100,blank=False,default='logo1')
    image=models.ImageField(upload_to='logo/',blank=False)

    def __str__(self):
        return self.title

class contactforms(models.Model):
    name=models.CharField(max_length=100,blank=False)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    message=models.TextField(max_length=300)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
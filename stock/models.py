from django.db import models

class Product (models.Model):
     name= models.CharField(max_length = 50)
     price= models.CharField(max_length=20)

class Client (models.Model):
    name= models.CharField(max_length = 50)
    cpf= models.CharField(max_length=20)

class Cart (models.Model):
     purchase_date= models.CharField(max_length = 20)
     client= models.CharField(max_length=20)
     client= models.ForeignKey(Product,on_delete=models.CASCADE)

class Amount(models.Model):
     amount=models.CharField(max_length = 20)
     product=models.CharField(max_length=30)
     cart= models.ForeignKey(Cart,on_delete=models.CASCADE, primary_key =True)


# Create your models here.

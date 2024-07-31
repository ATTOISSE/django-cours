from django.db import models as m
from uuid import uuid4

class Client(m.Model):
    id = m.AutoField(primary_key=True)
    email = m.EmailField()
    password = m.CharField()
    age = m.IntegerField(null=True)
    username = m.CharField(max_length=100)
    first_name = m.CharField(null=True,max_length=100)
    last_name = m.CharField(null=True,max_length=100)

class Order(m.Model):
    id = m.AutoField(primary_key=True)
    command_number = m.UUIDField(default=uuid4)
    created_at = m.DateTimeField(auto_now_add=True)
    client = m.ForeignKey(Client,on_delete=m.deletion.CASCADE,related_name='orders')

class Product(m.Model):
    wording = m.CharField(unique=True)
    price = m.FloatField()
    stock = m.SmallIntegerField(null=True)
    disponibility = m.BooleanField(null=True)
    description = m.TextField()
    picture = m.ImageField(upload_to='images/',null=True)
    command = m.ForeignKey(Order,on_delete=m.deletion.CASCADE,related_name='products',null=True)

    @property
    def is_disponibility(self):
        if not self.disponibility:
            return 'Indisponible'
        return 'Disponible'

class Category(m.Model):
    id = m.AutoField(primary_key=True)
    name = m.CharField(unique=True)
    products = m.ManyToManyField(Product,related_name='categories',null=True)





from django.db import models


class Header(models.Model):
    orderid = models.IntegerField(primary_key=True)
    customerid = models.IntegerField(primary_key=False)
    shipto_address = models.CharField(max_length=100)
    shipto_city = models.CharField(max_length=100)
    shipto_country = models.CharField(max_length=100)
    shipto_postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.orderid}-{self.customerid}'


class Item(models.Model):
    orderitemid = models.IntegerField(primary_key=True)
    orderid = models.IntegerField(primary_key=False)
    productid = models.IntegerField(primary_key=False)
    qty = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    vat = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Order:{self.orderid} Item:{self.orderitemid} Product:{self.productid} Qty:{self.qty}'



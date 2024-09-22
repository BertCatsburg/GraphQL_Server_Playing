from django.db import models


class Products(models.Model):
    productid = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.productid}'

from django.db import models

# Create your models here.


class ProductInfo(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    price = models.PositiveIntegerField()
    descriptions = models.TextField(null=True, blank=True)
    img = models.ImageField(default="product/default.png",
                            upload_to="product/", null=True, blank=True)

    def __str__(self):
        return self.name

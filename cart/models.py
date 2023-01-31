from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}"


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='static/products/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        img = img.resize((100, 100), Image.ANTIALIAS)
        img.save(self.image.path)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.cart}_{self.product}"


class NewModel(models.Model):
    time1 = models.DateTimeField()
    time2 = models.TimeField()
    time3 = models.DurationField()
    name = models.CharField(max_length=100)
    name1 = models.TextField()
    int = models.IntegerField()
    float = models.DecimalField(max_digits=7, decimal_places=2)
    file = models.FileField()
    email = models.EmailField()
    pic = models.ImageField()
    json = models.JSONField()
    b = models.BooleanField()

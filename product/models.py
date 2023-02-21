from django.utils import timezone
from django.db import models

# alows soft delete


class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)


class SoftDeleteModel(models.Model):

    deleted_at = models.DateTimeField(null=True, default=None, blank=True)
    objects = SoftDeleteManager()
    all_objects = models.Manager()

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()

    class Meta:
        abstract = True


# product model
class Product(SoftDeleteModel):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='images/', null=True, blank=True, default='/palceholder.png')

    def __str__(self):
        return self.name

# cart item model


class CartItem(SoftDeleteModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name

    def get_total(self):
        return self.product.price * self.quantity

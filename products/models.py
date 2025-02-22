from django.db import models


# Create your models here.
class Category(models.Model):
    
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(default=0)
    material = models.CharField(max_length=100, null=True, blank=True)
    glaze_type = models.CharField(max_length=100, null=True, blank=True)
    colour = models.CharField(max_length=50, null=True, blank=True)
    # Dimensions added directly, revise for scaleability
    # Stored as string to include units, revise for scaleability
    height = models.CharField(max_length=20, null=True, blank=True)  # Stored as string to include units
    opening_diameter = models.CharField(max_length=20, null=True, blank=True)
    diameter_at_widest_point = models.CharField(max_length=20, null=True, blank=True)
    base_diameter = models.CharField(max_length=20, null=True, blank=True)
    weight = models.CharField(max_length=20, null=True, blank=True)
    capacity = models.CharField(max_length=20, null=True, blank=True)
    # Image added directly, revise for multiple images & scaleability
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
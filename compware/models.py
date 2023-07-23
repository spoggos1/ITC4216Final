from django.db import models
from django.utils.html import mark_safe
# Create your models here.



class Category(models.Model):
    category = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.category}"


class Subcategory(models.Model):
    subcategory = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.subcategory}"


class Item(models.Model):
    item_name = models.CharField(max_length=100)
    item_price = models.CharField(max_length=100)
    item_image = models.ImageField(upload_to ='uploads/',blank=True)
    item_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="itemcategory")
    item_subcat = models.ForeignKey(Subcategory, on_delete=models.CASCADE,related_name="itemsubcategory")

    def __str__(self):
        return f"{self.item_name} <Price:> {self.item_price} <Category:> {self.item_category} <Subcategory:> {self.item_subcat}"
    
    def img_preview(self):
        return mark_safe(f'<img src = "{self.item_image.url}" width = "300"/>')
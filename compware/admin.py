from django.contrib import admin
from .models import Item, Category, Subcategory
# Register your models here.


admin.site.register(Subcategory)
admin.site.register(Category)

class ProductAdmin(admin.ModelAdmin): # new
     readonly_fields = ['img_preview']

admin.site.register(Item,ProductAdmin)
from itertools import product
from django.contrib import admin

# Register your models here.
from .models import Product,Order,Plan,Blog

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Plan)
admin.site.register(Blog)
from django.contrib import admin
from .models import Category, Colors, Size, Bike, Review, PurchaseRequest

admin.site.register(Category)
admin.site.register(Colors)
admin.site.register(Size)
admin.site.register(Bike)
admin.site.register(Review)
admin.site.register(PurchaseRequest)

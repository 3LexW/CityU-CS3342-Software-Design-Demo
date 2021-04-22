from django.contrib import admin
from .models import Product, shoppingCart, shoppingCartHistory

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "age_resticted", "price")


class ShoppingCartHistoryAdmin(admin.ModelAdmin):
    list_display = ("id", "shoppingCart", "item", "action")

admin.site.register(Product, ProductAdmin)
admin.site.register(shoppingCart)
admin.site.register(shoppingCartHistory, ShoppingCartHistoryAdmin)
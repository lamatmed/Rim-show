from django.contrib import admin
from .models import *
 
# Register your models here.
class AdminCategorie(admin.ModelAdmin):
    list_display =('name','date_added')
class AdminProduct(admin.ModelAdmin):
    list_display =('title','price','category', 'date_added')
class AdminCommande(admin.ModelAdmin):
    list_display =('items', 'nom','email','adresse','ville','pays','zipcode','date_commande')   
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategorie)
admin.site.register(Commande,AdminCommande)
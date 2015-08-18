from django.contrib import admin
from .models import Pizza

class PizzaAdmin(admin.ModelAdmin):
    search_fields = ['name', 'ingredients']
    list_display = ('name', 'price', 'ingredients', 'picture')

# Register your models here.
admin.site.register(Pizza, PizzaAdmin)

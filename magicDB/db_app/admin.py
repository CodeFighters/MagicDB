from django.contrib import admin
from .models import Lists, Groceries

# Register your models here.
@admin.register(Lists)
class ListsAdmin(admin.ModelAdmin):
	model = Lists

	list_display = ['name', ]


@admin.register(Groceries)
class GroceriesAdmin(admin.ModelAdmin):
	model = Groceries

	list_display = ['name', 'list_name', 'quantity', 'measurement', 'is_bought', ]

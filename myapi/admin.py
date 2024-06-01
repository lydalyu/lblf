from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.User)
admin.site.register(models.Nutrition)
admin.site.register(models.Unit)
admin.site.register(models.Cooking)
admin.site.register(models.CookingNutrition)
admin.site.register(models.UserNutrition)
admin.site.register(models.Category)
admin.site.register(models.Product)
admin.site.register(models.ProductNutrition)
admin.site.register(models.Dish)
admin.site.register(models.Meal)
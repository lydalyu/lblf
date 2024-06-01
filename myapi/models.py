from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django import forms
from django.db.models.functions import Now

class User(AbstractUser):
    pass

class Nutrition(models.Model):
    code = models.CharField(max_length=200)

    def __str__(self):
        return self.code
    
class Unit(models.Model):
    code = models.CharField(max_length=50)
    multiplier = models.IntegerField(default=1)
    base = models.BooleanField(default=False)
    
    def __str__(self):
        return self.code + ' - ' + str(self.multiplier)
    
class Cooking(models.Model):
    code = models.CharField(max_length=200)
    base_index = models.DecimalField(max_digits=19, decimal_places=10, default=1)

    def __str__(self):
        return self.code + ' ' + self.base_index

class CookingNutrition(models.Model):
    cooking = models.ForeignKey('Cooking', on_delete=models.CASCADE, related_name="cooking_type", related_query_name="cooked_nutrition_indexes")
    nutrition = models.ForeignKey('Nutrition', on_delete=models.CASCADE, related_name="nutrition", related_query_name="cooking_indexes")
    change_index = models.DecimalField(max_digits=19, decimal_places=10, default=1)

    def __str__(self):
        return self.cooking.code + ' ' + self.nutrition.code + ' ' + self.change_index
    
class UserNutrition(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="user_nutr", related_query_name="nutritions")
    nutrition = models.ForeignKey('Nutrition', on_delete=models.CASCADE, related_name="nutrition_type", related_query_name="users_nutrition")
    daily_value = models.DecimalField(max_digits=19, decimal_places=10, null=True)
    unit = models.ForeignKey('Unit', on_delete=models.CASCADE, related_name="unit", null=True, related_query_name="user_nutritions")

    def __str__(self):
        return self.user.username + ' schould eat ' + self.daily_value + self.unit.code + ' ' + self.nutrition.code + ' per a day.'
    
class Category(models.Model):
    code = models.CharField(max_length=200)
    image = models.ImageField(upload_to='category/', null=True)

    def __str__(self):
        return self.code

class Product(models.Model):
    name = models.CharField(max_length=200)
    max_gr_per_day = models.IntegerField(default=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name="category", default=0, related_query_name="products")
    supplement = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' in category ' + self.category.code + ' max ' + self.max_gr_per_day + ' per day.'
    
class ProductNutrition(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name="product_nutrition", related_query_name="product_nutritions")
    nutrition = models.ForeignKey('Nutrition', on_delete=models.CASCADE, related_name="nutrition_for_product", related_query_name="products_with_nutrition")
    value_per_100gr = models.DecimalField(max_digits=19, decimal_places=10)
    unit = models.ForeignKey('Unit', on_delete=models.CASCADE, related_name="unit_type", related_query_name="products_nutritions")

    def __str__(self):
        return self.product.name + ' contains ' + self.value_per_100gr + self.unit.code + ' per 100 gramm.'
    
class Dish(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name="category_for_dish", default=0, related_query_name="dishes")

class DishProduct(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name="product_in_dish", related_query_name="in_dishes")
    dish = models.ForeignKey('Dish', on_delete=models.CASCADE, related_name="dish_original", related_query_name="dish_products")
    weight = models.IntegerField(default=100)
    cooked_by = models.ForeignKey('Cooking', on_delete=models.CASCADE, related_name="dish_cooked_by", null=True, related_query_name="cooked_dishes")

    def __str__(self):
        return self.dish.name + ' contains ' + self.weight + 'gr of product ' + self.product.name + ' cooked by ' + self.cooked_by.code
    
class Meal(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="eater", related_query_name="meals")
    dish = models.ForeignKey('Dish', on_delete=models.CASCADE, related_name="dish_eated", null=True, related_query_name="eated_in_meals")
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name="product_eated", null=True, related_query_name="eated_in_meals")
    weight = models.IntegerField(default=100)
    cooked_by = models.ForeignKey('Cooking', on_delete=models.CASCADE, related_name="meal_cooked_by", null=True, related_query_name="cooked_meals")
    date = models.DateTimeField(default=Now())

    def __str__(self):
        return self.user.username + ' eated ' + self.dish.name + self.product.name + ' at ' + self.date
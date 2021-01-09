from django.contrib import admin
from .models import Recipe, Food, Ingredient

# Register your models here.
class IndredientInline(admin.TabularInline):
    model = Ingredient

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = (IndredientInline,)

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    pass


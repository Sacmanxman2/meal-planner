from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Conversion)
admin.site.register(Fraction)
admin.site.register(Unit)
admin.site.register(Ingredient)


admin.site.register(Step)


class RecipeIngredientsInline(admin.TabularInline):
    model = RecipeIngredient


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        RecipeIngredientsInline
    ]


admin.site.register(MealPlan)
admin.site.register(Meal)
admin.site.register(ShoppingList)

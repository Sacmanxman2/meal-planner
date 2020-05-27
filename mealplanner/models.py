from django.db import models


class Fraction(models.Model):
    """Custom data type for storing fractions"""
    numerator = models.IntegerField()
    denominator = models.IntegerField()

    def __str__(self):
        return "{0} / {1}".format(self.numerator, self.denominator)


class Unit(models.Model):
    """Unit labels"""
    name = models.CharField(null=True, max_length=128)
    abbreviation = models.CharField(null=True, max_length=64)
    unit_type = models.CharField(null=True, max_length=128)

    def __str__(self):
        return self.name


class Conversion(models.Model):
    """Conversions between units. `unit_conversion` will be null if it's an incompatible type (such as converting between volume and weight)"""
    unit_from = models.ForeignKey(
        Unit, related_name="unit_from", on_delete=models.CASCADE)
    unit_to = models.ForeignKey(
        Unit, related_name="unit_to", on_delete=models.CASCADE)
    unit_conversion = models.ForeignKey(
        Fraction, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return "{0} to {1}".format(self.unit_from.name, self.unit_to.name)


class Ingredient(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now=True)


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.ManyToManyField(
        Ingredient, through='RecipeIngredient')
    created_at = models.DateTimeField(auto_now=True)


class Step(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    order = models.IntegerField()
    description = models.TextField()


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    ingredient_amount = models.ForeignKey(
        Fraction, on_delete=models.PROTECT, null=True)
    ingredient_unit = models.ForeignKey(
        Unit, on_delete=models.PROTECT, null=True)


class MealPlan(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)


class Meal(models.Model):
    meal_plan = models.ForeignKey(MealPlan, on_delete=models.CASCADE)
    date = models.DateField()
    name = models.CharField(max_length=200)
    order = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)


class ShoppingList(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    ingredients = models.ManyToManyField(
        Ingredient, through='ShoppingListIngredient')


class ShoppingListIngredient(models.Model):
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.ForeignKey(Fraction, on_delete=models.PROTECT)
    checked = models.BooleanField(default=False)

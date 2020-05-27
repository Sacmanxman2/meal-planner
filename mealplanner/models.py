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

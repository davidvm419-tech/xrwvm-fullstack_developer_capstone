# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
class CarModel(models.Model):
    maker = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    MODELS = [
        ("SEDAN", "Sedan"),
        ("SUV", "SUV"),
        ("WAGON", "Wagon"),
        ]
    name = models.CharField(max_length=100, choices=MODELS, default="SUV")
    year = models.IntegerField(default=2023, validators=[MinValueValidator(2015), MaxValueValidator(2023)])

    def __str__(self):
        return self.name
# - __str__ method to print a car make object

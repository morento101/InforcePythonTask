from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import (
    MinValueValidator, MaxValueValidator, MinLengthValidator
)

Employee = get_user_model()


class Resturant(models.Model):
    """Resturant model, where employees can have a lunch."""

    name = models.CharField(max_length=20, validators=[MinLengthValidator(10)])
    description = models.TextField()


class Menu(models.Model):
    """Menu model which represent lunch in the rsturant for specific day."""

    class DayChoices(models.IntegerChoices):
        """This class is used for choosing a day when menu will be served."""

        MONDAY = 1, "Monday"
        TUESDAY = 2, "Tuesday"
        WEDNESDAY = 3, "Wednesday"
        THURSDAY = 4, "Thursday"
        FRIDAY = 5, "Friday"
        SATURDAY = 6, "Saturday"
        SUNDAY = 7, "Sunday"

    first_course = models.CharField(
        max_length=30, validators=[MinLengthValidator(3)]
    )
    main_course = models.CharField(
        max_length=30, validators=[MinLengthValidator(3)]
    )
    dessert = models.CharField(
        max_length=30, validators=[MinLengthValidator(3)]
    )
    drink = models.CharField(max_length=30, validators=[MinLengthValidator(3)])
    day = models.IntegerField(choices=DayChoices.choices)
    resturant = models.ForeignKey(Resturant, on_delete=models.CASCADE)


class Review(models.Model):
    """Review that can be posted by employee to rate menu."""

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    rating = models.IntegerField(
        blank=False, validators=(MinValueValidator(0), MaxValueValidator(5)),
    )
    description = models.TextField(blank=True, null=True)

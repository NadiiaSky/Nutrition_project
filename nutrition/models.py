from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

GENDER_CHOICES = (
    (1, "Male"),
    (2, "Female")
)

BLOOD_TYPE_CHOICES = (
    ('First', (
        ('+', 'Positive'),
        ('-', 'Negative'),
    )),
    ('Second', (
        ('+', 'Positive'),
        ('-', 'Negative'),
    )),
    ('Third', (
        ('+', 'Positive'),
        ('-', 'Negative'),
    )),
    ('Fourth', (
        ('+', 'Positive'),
        ('-', 'Negative'),
    ))
)

NUTRITION_CHOICES = (
    ('loss_weight', 'Loss weight'),
    ('balance', 'Balance'),
    ('mass_weight', 'Mass weight')
)


class MedicalInfo(models.Model):
    blood_type = models.CharField(choices=BLOOD_TYPE_CHOICES, max_length=20)
    allergies = models.CharField(max_length=120)
    notes = models.CharField(max_length=120)
    condition = models.CharField(max_length=120)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    medical_info = models.OneToOneField(MedicalInfo, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    height = models.IntegerField()
    weight = models.FloatField()
    daily_calories = models.IntegerField()
    actual_calories = models.IntegerField()

    program = models.ForeignKey('Program', on_delete=models.SET_NULL, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('profile-detail', args=[self.id])


class Product(models.Model):
    name = models.CharField(max_length=120)
    calories = models.FloatField()


class Program(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, default="Program")
    formula = models.IntegerField()
    ration = models.CharField(max_length=120)
    duration = models.DurationField()
    calories = models.IntegerField()
    prohibitedFoods = models.CharField(max_length=120)
    training = models.IntegerField()
    water = models.FloatField()
    time_of_sleep = models.IntegerField()
    activity = models.IntegerField()

    def __str__(self):
        return self.name


class Nutrition(models.Model):
    products = models.ManyToManyField(Product)
    type = models.CharField(choices=NUTRITION_CHOICES, max_length=20)

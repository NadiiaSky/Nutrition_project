import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from nutrition.models import Product, Profile, MedicalInfo, Program, Nutrition


class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="potato", calories=133)
        Product.objects.create(name="water", calories=15)

    def test_product(self):
        potato = Product.objects.get(name='potato')
        water = Product.objects.get(name='water')
        self.assertEqual(potato.name, 'potato')
        self.assertEqual(potato.calories, 133)
        self.assertEqual(water.calories, 15)


class ProfileTestCase(TestCase):
    def setUp(self):
        user = User(username='nadiia')
        medical_info = MedicalInfo(
            blood_type="First",
            allergies="orange",
            notes="don't kile seafood",
            condition="good",
        )
        user.save()
        medical_info.save()
        Profile.objects.create(user=user, gender=1, height=170, weight=55, daily_calories=2000, actual_calories=2100,
                               medical_info=medical_info)

    def test_user_profile(self):
        nadiia = Profile.objects.get(user__username='nadiia')
        self.assertEqual(nadiia.user.username, 'nadiia')


class MedicalInfoTestCase(TestCase):
    def setUp(self):
        MedicalInfo.objects.create(blood_type="Third +", allergies="tarragon", notes="very love red fish",
                                   condition="normal")
        MedicalInfo.objects.create(blood_type="Fourth +", allergies="None", notes="don't like mushrooms",
                                   condition="sick")

    def test_blood_info(self):
        third_blood = MedicalInfo.objects.get(blood_type="Third +")
        fourth_blood = MedicalInfo.objects.get(blood_type="Fourth +")
        self.assertEqual(third_blood.blood_type, "Third +")
        self.assertEqual(fourth_blood.blood_type, "Fourth +")

    def test_medical_info(self):
        patient1 = MedicalInfo.objects.get(allergies="None", condition="sick")
        patient2 = MedicalInfo.objects.get(allergies="tarragon", condition="normal")
        self.assertEqual(patient1.allergies, "None")
        self.assertEqual(patient2.allergies, "tarragon")

        self.assertEqual(patient1.condition, "sick")
        self.assertEqual(patient2.condition, "normal")


class ProgramTestCase(TestCase):
    def setUp(self):
        Program.objects.create(name="smooth start", duration=datetime.timedelta(days=20, hours=10), calories=1980,
                               water=2.1, time_of_sleep=8, formula=30, training=45, activity=4350)

    def test_program(self):
        program1 = Program.objects.get(name="smooth start", duration=datetime.timedelta(days=20, hours=10),
                                       calories=1980, water=2.1,
                                       time_of_sleep=8)
        self.assertEqual(program1.name, "smooth start")
        self.assertEqual(program1.calories, 1980)


class NutritionTestCase(TestCase):
    def setUp(self):
        product = Product(name="potato", calories=133)
        product.save()

        nutrition = Nutrition(type="balance")
        nutrition.save()
        nutrition.products.set([product])
        nutrition.save()

    def test_nutrition(self):
        potato = Nutrition.objects.get(products__name="potato", type="balance")
        self.assertEqual(potato.products.first().name, "potato")
        self.assertEqual(potato.type, "balance")

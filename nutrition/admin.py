from django.contrib import admin
from .models import Nutrition, Product, Profile, Program, MedicalInfo


# Register your models here.
admin.site.register(Nutrition)
admin.site.register(Product)
admin.site.register(Profile)
admin.site.register(Program)
admin.site.register(MedicalInfo)

from django.forms import ModelForm

from nutrition.models import Profile, MedicalInfo


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('id', 'user', 'medical_info')


class MedicalInfoForm(ModelForm):
    class Meta:
        model = MedicalInfo
        exclude = ('id', )

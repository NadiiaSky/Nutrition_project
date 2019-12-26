from django.forms import ModelForm

from nutrition.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('id', 'user', 'medical_info')

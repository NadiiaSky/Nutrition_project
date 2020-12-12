from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from nutrition.forms import ProfileForm, MedicalInfoForm
from nutrition.models import Profile, MedicalInfo


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class ProfileDetailView(generic.DetailView):
    model = Profile


class ProfileUpdate(generic.UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name_suffix = '_update_form'


class MedicalInfoUpdate(generic.UpdateView):
    model = MedicalInfo
    form_class = MedicalInfoForm
    template_name = 'nutrition/medical_info_update_form.html'

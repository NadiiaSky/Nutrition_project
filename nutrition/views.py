from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from nutrition.forms import ProfileForm
from nutrition.models import Profile


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

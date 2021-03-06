from django.urls import path

from nutrition.views import ProfileDetailView, ProfileUpdate, MedicalInfoUpdate
from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('<int:pk>/update', ProfileUpdate.as_view(), name='profile-update'),
    path('medical-info/<int:pk>/update', MedicalInfoUpdate.as_view(), name='medical-info-update'),
]

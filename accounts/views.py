from .forms import CustomUserCreationForm
from .models import CustomUser
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import CreateView
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    models = CustomUser
    template_name = 'registration/sign_up.html'
    success_url = reverse_lazy('home')

class LoginUser(LoginView):
    template_name = 'registration/login.html'
    model = CustomUser
class LogoutUser(LogoutView):
    template_name = 'registration/logout.html'
    success_url = reverse_lazy('logout')
    model = CustomUser
    
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username','first_name','last_name','email','age','phone_number','password1','password2')
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username','email','age','phone_number')

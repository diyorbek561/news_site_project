from django.contrib import admin
from .forms import CustomUserCreationForm,CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username','first_name','last_name','age','phone_number','is_staff')
    fieldsets = UserAdmin.fieldsets + (
    (None,{"fields":('age','phone_number'),}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{"fields":('username','first_name','last_name','age','phone_number','password1','password2'),}),
    )
    ordering = ['-id']
admin.site.register(CustomUser,CustomUserAdmin)


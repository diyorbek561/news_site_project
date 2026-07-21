from django.urls import path
from .views import SignUpView,LoginUser,LogoutUser
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutUser.as_view(), name='logout'),
]
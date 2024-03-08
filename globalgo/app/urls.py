
from django.urls import path
from .views import *

urlpatterns = [
    path('',login),
    path('signup/',signup, name="signup"),
    path('staffsignup/',staff_signup, name="staffsignup"),
    path('user_register/',UserRegister, name="user_register"),
    path('admin_view/',adminView, name="admin_view"),
    path('staff_register/',staffRegister, name="staff_register"),
   
   
]

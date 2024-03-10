
from django.urls import path
from .views import *
from .controler_logic import *

urlpatterns = [
    path('',signin),
    path('sigin/',login_logic, name="sigin"),
    path("logout/", logout_view, name="logout"),
    path('check_authentication/',check_authentication,name='check_authentication'),
    path('signup/',signup, name="signup"),
    path('staffsignup/',staff_signup, name="staffsignup"),
    path('user_register/',UserRegister, name="user_register"),
    path('admin_view/',adminView, name="admin_view"),
    path('staff_register/',staffRegister, name="staff_register"),
    path('staff_view/<int:staff_id>/',staff_details, name="staff_view"),
    path('staff_edit/<int:staff_id>/',edit_staff_details, name="staff_edit"),
    path('view_staff_customers/<int:staff_id>/',view_staff_customers, name="view_staff_customers"),
    path('change_password/',view_change_password, name='change_password'),
    path('otp_verification_mail/', view_otp_verification, name='otp_verification_mail'),
     path('otp_verification/', verify_otp, name='otp_verification'),

    # path('reset_password/<int:user_id>/', views.reset_password, name='reset_password'),
    

]

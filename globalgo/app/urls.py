
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
    path('staff_register/',staffRegister, name="staff_register"),
    path('profile_view/<int:user_id>/',staff_details, name="profile_view"),
    path('profile_edit/<int:user_id>/',edit_staff_details, name="profile_edit"),
    path('view_staff_customers/<int:staff_id>/',view_staff_customers, name="view_staff_customers"),
    path('change_password/',view_change_password, name='change_password'),
    path('otp_verification_mail/', view_otp_verification, name='otp_verification_mail'),
    path('otp_verification/', verify_otp, name='otp_verification'),
    path('reset_password/', verify_email_resertpassword, name='reset_password'),
    path('reset_password_link/', verify_email_link, name='reset_password_link'),
    path('reset_user_password/<str:token>/', resert_change_password, name='reset_user_password'),
    path('passwordReset/', password_reset, name='passwordReset'),
    path('change_user_password/',change_user_password , name='change_user_password'),
    path('admin_view/',adminView, name="admin_view"),
    path('student_view/',student_view , name='student_view'),
    path('staff_view/',student_view , name='staff_view'),
    path('usa_services/',usa_service_view , name='usa_services'),
    path('visito_visa_application/',visito_visa_application , name='visito_visa_application'),
    path('update_profile_details/<int:user_id>/',update_profile_details, name="update_profile_details"),
    path('updateprofile/',updateprofile, name="updateprofile"),
    
    

]

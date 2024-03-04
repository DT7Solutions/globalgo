from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login

from .models import *
# from apps.home.constants import user_login_roles



def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        msg = None
        try:
            user = authenticate(email=username, password=password)
            if user is not None and user.is_active:
                user_role = UserRole.objects.filter(user=user).first()
                if user_role:
                    if user_role.role.name == "admin":
                        # Redirect to admin page or set appropriate permissions.
                        print('admin')
                    elif user_role.role.name == "staff":
                        # Redirect to staff page or set appropriate permissions.
                        print("staff")
                    else:
                        # Redirect to student page or set appropriate permissions.
                        print("student")

                login(request, user)
                return redirect("/")
            else:
              
                msg = 'Invalid credentials'
        except Exception as e:
            msg = 'An error occurred while processing your request'
    return render(request, 'uifiles/login.html')
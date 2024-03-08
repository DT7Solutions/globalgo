
from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from .models import *
from django.contrib import messages
# from apps.home.constants import user_login_roles



def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        msg = None
        try:
            user = authenticate(email=username, password=password)
            if user is not None and user.is_active:
                if user:
                    if user.role.name == "admin":
                        # Redirect to admin page or set appropriate permissions.
                        print('admin')
                        return redirect("/admin_view/")
                    elif user.role.name == "staff":
                        # Redirect to staff page or set appropriate permissions.
                        print("staff")
                    else:
                        # Redirect to student page or set appropriate permissions.
                        print("student")
                        

                # login(request, user)
                
            else:
              
                msg = 'Invalid credentials'
        except Exception as e:
            msg = 'An error occurred while processing your request'
    return render(request, 'uifiles/login.html')


def signup(request):
    return render(request, 'uifiles/signup.html')
def staff_signup(request):
    return render(request, 'uifiles/staffregister.html')

def adminView(request):
    context = {}
    staff_users = Users.objects.filter(role__name="staff")  
    context['users'] = staff_users 
    return render(request, 'uifiles/admin.html',context)

@csrf_exempt
def UserRegister(request):
    if request.method == 'POST':
        try:
            user_name = request.POST.get("username")
            phone = request.POST.get("phone")
            user_email = request.POST.get("emailId")
            password = request.POST.get("password")
            confirm_password = request.POST.get("confirm_password")
           
            if password != confirm_password:
                return JsonResponse({'message': 'Passwords do not match.'}, status=400)

            if Users.objects.filter(username=user_name).exists():
                return JsonResponse({'message': 'Username already exists.'}, status=400)
            
            if Users.objects.filter(email=user_email).exists():
                return JsonResponse({'message': 'Email already exists.'}, status=400)
            roledata = Role.objects.all()
            new_user = Users()
            new_user.username=user_name
            new_user.email=user_email
            new_user.password=make_password(password)
            new_user.phone = phone
            new_user.created_at = datetime.now()
            new_user.is_active = True
            new_user.is_staff = True
            new_user.is_superuser = False
            new_user.role = roledata[2]
            new_user.save()
        
            

            return JsonResponse({'message': 'User registered successfully.'})
        except KeyError:
            return JsonResponse({'message': 'Invalid request parameters.'}, status=400)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)
    else:
        return JsonResponse({'message': 'Method not allowed.'}, status=405)


@csrf_exempt
def staffRegister(request):
    if request.method == 'POST':
        try:
            user_name = request.POST.get("username")
            phone = request.POST.get("phone")
            user_email = request.POST.get("emailId")
            password = request.POST.get("password")
            confirm_password = request.POST.get("confirm_password")
           
            if password != confirm_password:
                return JsonResponse({'message': 'Passwords do not match.'}, status=400)

            if Users.objects.filter(username=user_name).exists():
                return JsonResponse({'message': 'Username already exists.'}, status=400)
            
            if Users.objects.filter(email=user_email).exists():
                return JsonResponse({'message': 'Email already exists.'}, status=400)
            roledata = Role.objects.all()
            new_user = Users()
            new_user.username=user_name
            new_user.email=user_email
            new_user.password=make_password(password)
            new_user.phone = phone
            new_user.created_at = datetime.now()
            new_user.is_active = True
            new_user.is_staff = True
            new_user.is_superuser = False
            new_user.role = roledata[1]
            new_user.save()
        
            

            return JsonResponse({'message': 'Staff registered successfully.'})
        except KeyError:
            return JsonResponse({'message': 'Invalid request parameters.'}, status=400)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)
    else:
        return JsonResponse({'message': 'Method not allowed.'}, status=405)


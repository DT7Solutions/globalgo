

from django import template
from django.template import loader
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import *
from .healper import send_otp_email_notification
from django.contrib import messages




def signin(request):
    context ={}
    try:
        return render(request, 'uifiles/login.html')
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(context, request))

def signup(request):
    return render(request, 'uifiles/signup.html')

@login_required
def staff_signup(request):
    context ={}
    try:
        return render(request, 'uifiles/staffregister.html')
    
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(context, request))


@login_required
def logout_view(request):
    try:
        logout(request)
        return redirect('/')
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(request))
      
@login_required
def adminView(request):
    context = {}
    staff_users = Users.objects.filter(role__name="staff")  
    context['users'] = staff_users 
    return render(request, 'uifiles/admin.html',context)

@login_required
def staff_details(request, staff_id):
    context = {}
    try:
        context['staff'] = Users.objects.filter(id=staff_id)
        return render(request, 'uifiles/staff_details.html',context)
    
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html',context)
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(context, request))

@login_required
def edit_staff_details(request, staff_id):
    context = {}
    try:
        context['edit_staff'] = Users.objects.filter(id=staff_id)
        return render(request, 'uifiles/edit_staff.html',context)
    
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(context, request))
    
@login_required
def view_staff_customers(request, staff_id):
    context = {}
    try:
        context['staff_customer'] = Users.objects.filter(id=staff_id)
        return render(request, 'uifiles/view_staf_customers.html',context)
    
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(context, request))
    
@login_required
def view_otp_verification(request):
    context = {}
    try:
        usenamename = request.user.username
        emailId = request.user.email
        send_otp_email_notification(request, name=usenamename, emailid=emailId)
        return render(request, 'uifiles/otp_verification.html',context)
     
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(context, request))
    
@login_required
def view_change_password(request):
    context = {}
    try:
        
        return render(request, 'uifiles/change_password.html',context)
    
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(context, request))
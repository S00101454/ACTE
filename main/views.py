from .forms import NewUserForm, SchoolInfoForm, UpdateUserForm
from .models import Project, School

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, Http404
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, login, authenticate 
from django.contrib.auth.models import User

def homepage(request):
    form = None
    schools = None
    projects = None
    if request.user.is_authenticated:
        if request.user.is_superuser:
            pass
        elif request.user.is_staff:
            schools = School.objects.all()
            projects = Project.objects.all()
        else:    
            if request.method == "POST":
                form = SchoolInfoForm(data=request.POST)
                if form.is_valid():
                    form = form.save(commit = False)
                    form.studentsAttending = 0
                    form = form.save()
            else:
                form = SchoolInfoForm(initial={"contact_email": str(request.user.email)})
    return render(request = request,
        template_name = "main/landing.html",
        context={"form":form, "schools":schools, "projects":projects})

def account_page(request):
    if not request.user.is_authenticated:
        return redirect("main:homepage")
    if request.method == "POST":
        form = UpdateUserForm(data=request.POST, instance=request.user)
        if form.is_valid():
            messages.success(request, f"Account updated successfully.")
            update = form.save(commit=False)
            update.user = request.user
            update.save()
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    else:
        form=UpdateUserForm(instance=request.user)

    return render(
        request = request,
        template_name = "main/account.html",
        context={"form":form}
    )

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"successfully logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(
        request = request,
        template_name = "main/login.html",
        context = {"form":form}
    )

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("main:account")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request = request,
            template_name = "main/register.html",
            context = {"form":form})

    form = NewUserForm
    return render(
        request = request,
        template_name = "main/register.html",
        context={"form":form}
    )

def logout_request(request):
    logout(request)
    messages.info(request, "Successfully logged out.")
    return redirect("main:homepage")

def judge_page(request):
    if not request.user.is_staff:
        raise PermissionDenied()
    return render(
        request = request,
        template_name = "main/judge.html",
        context = {"schools": School.objects.all()}
    )

def admin_page(request):
    if not request.user.is_superuser:
        raise PermissionDenied()
    return render(
        request = request,
        template_name = "main/adminpage.html",
        context = {}
    )

def scoring_page(request, id=None):
    if request.user.is_authenticated and request.user.is_staff:
        try:
            project = Project.objects.get(front_end_id=id)
        except ObjectDoesNotExist:
            raise Http404("Project does not exist")        
        return render(
        request = request,
        template_name = "main/scoring.html",
        context = {"project":project}
    )
    else:
       raise PermissionDenied()
    
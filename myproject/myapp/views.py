from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, LoginForm
from .models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                if user.user_type == 'patient':
                    return redirect('patient_dashboard')  
                elif user.user_type == 'doctor':
                    return redirect('doctor_dashboard')
            else:
                return redirect(request, 'myapp/login_failed.html')
    else:
        form = LoginForm()
    return render(request, 'myapp/login.html', {'form':form})

def user_logout(request):
    logout(request)
    form = LoginForm()
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST, request.FILES)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            form = LoginForm()
            return redirect('login')
    else:
        user_form = SignUpForm()
    return render(request, 'myapp/register.html', {'user_form':user_form})

@login_required
def doctor_dashboard(request):
    user = request.user
    return render(request, 'myapp/doctor_dashboard.html', {'user': user})

@login_required
def patient_dashboard(request):
    user = request.user
    return render(request, 'myapp/patient_dashboard.html', {'user': user})
    
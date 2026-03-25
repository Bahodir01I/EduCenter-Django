from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import StudentSignUpForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Welcome to EduCenter, {user.username}! Your account has been created.")
            return redirect('dashboard')
    else:
        form = StudentSignUpForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def dashboard(request):
    context = {}
    if request.user.role == 'admin':
        from courses.models import Course
        from enrollments.models import Enrollment
        from .models import User
        context['student_count'] = User.objects.filter(role='student').count()
        context['course_count'] = Course.objects.count()
        context['enrollment_count'] = Enrollment.objects.count()
    return render(request, 'users/dashboard.html', context)

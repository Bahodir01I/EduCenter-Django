from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Course, Category
from enrollments.models import Enrollment

def course_list(request):
    query = request.GET.get('q', '')
    category_id = request.GET.get('category', '')
    
    courses = Course.objects.all().order_by('-created_at')
    
    if query:
        courses = courses.filter(
            Q(title__icontains=query) | 
            Q(description__icontains=query) |
            Q(instructor__username__icontains=query)
        )
    if category_id:
        courses = courses.filter(category_id=category_id)
        
    paginator = Paginator(courses, 6) # 6 courses per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    categories = Category.objects.all()
    
    context = {
        'page_obj': page_obj,
        'categories': categories,
        'query': query,
        'current_category': category_id,
    }
    return render(request, 'courses/course_list.html', context)

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    enrolled = False
    if request.user.is_authenticated and request.user.role == 'student':
        enrolled = Enrollment.objects.filter(student=request.user, course=course).exists()
        
    context = {
        'course': course,
        'enrolled': enrolled,
    }
    return render(request, 'courses/course_detail.html', context)

@login_required
def enroll_course(request, pk):
    if request.user.role != 'student':
        messages.error(request, "Only students can enroll in courses.")
        return redirect('course_detail', pk=pk)
        
    course = get_object_or_404(Course, pk=pk)
    enrollment, created = Enrollment.objects.get_or_create(
        student=request.user, 
        course=course,
        defaults={'status': 'active'}
    )
    
    if created:
        messages.success(request, f"You have successfully enrolled in {course.title}!")
    else:
        messages.info(request, "You are already enrolled in this course.")
        
    return redirect('dashboard')

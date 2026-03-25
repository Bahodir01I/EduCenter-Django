from rest_framework import viewsets, permissions
from users.models import User
from courses.models import Course
from enrollments.models import Enrollment
from .serializers import StudentSerializer, CourseSerializer, EnrollmentSerializer

class StudentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.filter(role='student')
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all().order_by('-created_at')
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EnrollmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Enrollment.objects.all().order_by('-enrollment_date')
    serializer_class = EnrollmentSerializer
    permission_classes = [permissions.IsAdminUser] # Only admins can see all enrollments

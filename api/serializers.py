from rest_framework import serializers
from users.models import User
from courses.models import Course, Category
from enrollments.models import Enrollment

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'date_joined']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class CourseSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    instructor = serializers.StringRelatedField()

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'category', 'instructor', 'price', 'level', 'duration', 'created_at']

class EnrollmentSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField()
    course = serializers.StringRelatedField()
    
    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'course', 'status', 'enrollment_date']


from django.shortcuts import render
from .models import Student

def search_courses(request):
    if request.method == 'GET' and 'student_name' in request.GET:
        student_name = request.GET['student_name']
        student = Student.objects.filter(name__icontains=student_name).first()
        if student:
            courses = student.courses.all()
        else:
            courses = []
        return render(request, 'course_list.html', {'courses': courses, 'student': student})
    return render(request, 'search_form.html')

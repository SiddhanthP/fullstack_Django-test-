from django.shortcuts import render
from django.http import JsonResponse
from .models import Course, Student

def homefun(request):
    courses = Course.objects.all()
    studentDetails = Student.objects.all()
    return render(request, 'course_list.html', {'courses': courses, 'students': studentDetails})

def formfun(request):
    if request.method == 'POST':
        name = request.POST.get('sname')
        email = request.POST.get('semail')
        course_name = request.POST.get('scourse')

        course, created_course = Course.objects.get_or_create(name=course_name)
        student, created_student = Student.objects.get_or_create(name=name, email=email)

        if course not in student.courses.all():
            student.courses.add(course)
            created = True
        else:
            created = False

        if created:
            message = f'{student.name} registered successfully for {course.name}.'
        else:
            message = f'{student.name} is already registered for {course.name}.'

        return JsonResponse({'message': message, 'status': 'success'})

    return render(request, 'student_registration.html')

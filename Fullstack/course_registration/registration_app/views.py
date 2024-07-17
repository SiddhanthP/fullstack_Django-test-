from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Course, Student

class CourseListView(ListView):
    model = Course
    template_name = 'course_list.html'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'


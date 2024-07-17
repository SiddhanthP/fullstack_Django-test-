from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.CourseListView.as_view(), name='course_list'),
    path('student/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
]

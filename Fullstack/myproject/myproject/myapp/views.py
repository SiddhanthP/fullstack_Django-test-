from django.shortcuts import render
from .models import Student
from .utils import generate_csv_response, generate_pdf_response

def generate_csv_view(request):
    queryset = Student.objects.all()
    response = generate_csv_response(queryset, 'students_data')
    return response

def generate_pdf_view(request):
    queryset = Student.objects.all()
    response = generate_pdf_response(queryset, 'students_data')
    return response
 
def index_view(request):
    return render(request, 'index.html')


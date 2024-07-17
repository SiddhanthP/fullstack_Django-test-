import csv
from django.http import HttpResponse
from reportlab.pdfgen import canvas

def generate_csv_response(queryset, filename):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{filename}.csv"'

    writer = csv.writer(response)
    writer.writerow([field.name for field in queryset.model._meta.fields])

    for obj in queryset:
        writer.writerow([getattr(obj, field.name) for field in queryset.model._meta.fields])

    return response

def generate_pdf_response(queryset, filename):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{filename}.pdf"'

    pdf = canvas.Canvas(response)
    y = 800

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(100, y, "Student Data")
    y -= 20
    
    pdf.setFont("Helvetica", 10)
    for obj in queryset:
        data = f"Name: {obj.name}, Email: {obj.email}"
        pdf.drawString(100, y, data)
        y -= 15

    pdf.showPage()
    pdf.save()

    return response

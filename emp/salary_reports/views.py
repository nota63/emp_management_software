from django.shortcuts import render, redirect
from .forms import Salary_Form
from .models import Salary
from django.contrib import messages
import io
from django.http import HttpResponse
from PIL import Image, ImageDraw, ImageFont


def generate_salary_reports(request):
    if request.method == 'POST':
        form = Salary_Form(request.POST)
        if form.is_valid():
            emp_name = form.cleaned_data['emp_name']
            emp_role = form.cleaned_data['emp_role']
            salary_credited = form.cleaned_data['salary_credited']
            payment_method = form.cleaned_data['payment_method']
            date = form.cleaned_data['date']
            salary_data = Salary(emp_name=emp_name, emp_role=emp_role, salary_credited=salary_credited,
                                 payment_method=payment_method, date=date)
            salary_data.save()
            messages.success(request, 'Salary credited done!')

            # Create an image
            width, height = 800, 600
            image = Image.new('RGB', (width, height), 'white')
            draw = ImageDraw.Draw(image)

            # Add colorful background
            draw.rectangle([(0, 0), (width, height)], fill='lightblue')

            # Add company logo
            logo_path = 'static/my.png'  # Update with your logo path
            logo = Image.open(logo_path)
            logo = logo.resize((100, 50))  # Resize logo if necessary
            image.paste(logo, (50, 20))

            # Add text details using default font
            font = ImageFont.load_default()

            draw.text((50, 100), f"Employee Name: {emp_name}", fill="black", font=font)
            draw.text((50, 140), f"Employee Role: {emp_role}", fill="black", font=font)
            draw.text((50, 180), f"Salary Credited: {salary_credited}", fill="black", font=font)
            draw.text((50, 220), f"Payment Method: {payment_method}", fill="black", font=font)
            draw.text((50, 260), f"Date: {date}", fill="black", font=font)

            # Add "Powered by Django" logo at the end
            django_logo_path = 'static/django.jpeg'  # Update with your Django logo path
            django_logo = Image.open(django_logo_path)
            django_logo = django_logo.resize((200, 50))  # Resize Django logo if necessary
            image.paste(django_logo, (width - 250, height - 70))

            # Save the image to a buffer
            buffer = io.BytesIO()
            image.save(buffer, format='PNG')
            buffer.seek(0)

            response = HttpResponse(buffer, content_type='image/png')
            response['Content-Disposition'] = 'attachment; filename="salary_report.png"'
            return response
    else:
        form = Salary_Form()
    return render(request, 'salary_reports/generate_salary_reports.html', {'form': form})


# check transaction history
def check_history(request):
    salary_data=Salary.objects.all()
    if request.method == 'POST':
        Salary.objects.all().delete()
        messages.success(request,'History deleted from the database')
        return redirect('check_history')
    return render(request,'salary_reports/history.html',{'salary_data':salary_data})








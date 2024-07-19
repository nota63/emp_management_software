from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from salaries.models import Salaries
from notice_board.models import Notice
from leaves_for.models import Leaves_for
import time
import datetime
from PIL import Image, ImageDraw, ImageFont
import os
from django.conf import settings


def home(request):
    return render(request, 'home.html')


def owner_login(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        if id == '1111':
            messages.success(request, 'owner logged in successfully')
            return redirect('owner_dashboard')
        else:
            messages.error(request, 'invlid credentials')
            return redirect('owner_login')
    return render(request, 'owner_login.html')


def owner_dashboard(request):
    return render(request, 'owner_dashboard.html')


def employee_attendance(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        if role == 'manager':
            return redirect('manager_login_view')

        elif role == 'developer':
            return redirect('developer_login_view')

        elif role == 'hr':
            return redirect('hr_login_view')

        elif role == 'sales':
            return redirect('sales_login_view')

        elif role == 'marketing':
            return redirect('marketing_login_view')

        elif role == 'support':
            return redirect('support_login_view')

        elif role == 'accountant':
            return redirect('accountant_login_view')

        elif role == 'admin':
            return redirect('admin_login_view')

        elif role == 'it_support':
            return redirect('it_support_login_view')

        elif role == 'project_manager':
            return redirect('project_manager_view')

        elif role == 'designer':
            return redirect('designer_login_view')

        elif role == 'product_manager':
            return redirect('product_manager_view')

        elif role == 'operations':
            return redirect('operations_login_view')

        elif role == 'executive':
            return redirect('executive_login_view')

        elif role == 'intern':
            return redirect('intern_login_view')

        elif role == 'security':
            return redirect('security_login_view')

        elif role == 'piun':
            return redirect('piun_login_view')

        elif role == 'cleaner':
            return redirect('cleaner_login_view')

    return render(request, 'employee_attendance.html')


def employee_salaries(request):
    salaries = Salaries.objects.all()
    return render(request, 'employee_salaries.html', {'salaries': salaries})


def notice_board(request):
    notices = Notice.objects.all()
    return render(request, 'notice_board.html', {'notices': notices})


def get_leaves(request):
    leaves = Leaves_for.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        role = request.POST.get('role')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        days = request.POST.get('days')
        date = request.POST.get('date')
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
        status = request.POST.get('status')
        data = Leaves_for(name=name, role=role, email=email, subject=subject, days=days, date=date, from_date=from_date,
                          to_date=to_date, status=status)
        data.save()
        messages.success(request, 'Application submitted!')
        return redirect('view_leaves')
    return render(request, 'get_leaves.html')


def view_leaves(request):
    leaves = Leaves_for.objects.all()
    return render(request, 'view_leaves.html', {'leaves': leaves})


def delete_leave(request, leave_id):
    leaves = get_object_or_404(Leaves_for, id=leave_id)
    leaves.delete()
    messages.success(request, "Leave application canceled!")
    return redirect('view_leaves')


# HR PAGE EMPLOYEE ID CARD
def create_and_view_id_card(request):
    if request.method == 'POST':
        emp_name = request.POST.get('emp_name')
        emp_role = request.POST.get('emp_role')
        emp_id = request.POST.get('emp_id')
        photo = request.FILES.get('photo')

        if emp_name and emp_role and emp_id and photo:
            try:
                # Save the uploaded photo temporarily
                photo_path = os.path.join(settings.MEDIA_ROOT, photo.name)
                with open(photo_path, 'wb+') as destination:
                    for chunk in photo.chunks():
                        destination.write(chunk)

                # Generate the ID card
                card = generate_id_card(emp_name, emp_role, emp_id, photo_path)

                # Save the ID card image
                id_card_path = os.path.join(settings.MEDIA_ROOT, f"{emp_id}_id_card.png")
                card.save(id_card_path)

                # Clean up the temporary photo file
                os.remove(photo_path)

                messages.success(request, f"ID Card created for {emp_name}!")
                return render(request, 'view_id_card.html', {'id_card_path': f"{emp_id}_id_card.png"})

            except Exception as e:
                messages.error(request, f"Error generating ID card: {e}")

    return render(request, 'create_id_card.html')


def generate_id_card(emp_name, emp_role, emp_id, photo_path):
    # Define card size and background color
    card_width, card_height = 400, 250
    background_color = (255, 255, 255)  # white background

    # Create a blank image with the background color
    card = Image.new('RGB', (card_width, card_height), background_color)
    draw = ImageDraw.Draw(card)

    # Load a font
    font_path = os.path.join(settings.BASE_DIR, 'arial.ttf')  # Ensure arial.ttf is in your BASE_DIR
    bold_font_path = os.path.join(settings.BASE_DIR, 'arialbd.ttf')  # Ensure arialbd.ttf is in your BASE_DIR
    font = ImageFont.truetype(font_path, 20)
    bold_font = ImageFont.truetype(bold_font_path, 24)

    # Draw text on the card
    draw.text((20, 20), "Employee ID Card", font=bold_font, fill="black")
    draw.text((20, 60), f"Name: {emp_name}", font=font, fill="black")
    draw.text((20, 100), f"Role: {emp_role}", font=font, fill="black")
    draw.text((20, 140), f"ID: {emp_id}", font=font, fill="black")

    # Add employee photo
    try:
        photo = Image.open(photo_path)
        photo = photo.resize((100, 100))
        card.paste(photo, (280, 20))
    except Exception as e:
        print(f"Error loading photo: {e}")

    return card


def hr_page(request):
    return render(request, 'hr_page.html')


# about page
def coming_soon(request):
    return render(request,'coming_soon.html')





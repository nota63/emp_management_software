from django.shortcuts import render,redirect
from .models import ContactUs
from .forms import ContactForm
from django.contrib import messages
import pyttsx3
# Create your views here.

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            contact=form.cleaned_data['contact']
            message=form.cleaned_data['message']
            data=ContactUs(name=name,email=email,contact=contact,message=message)
            data.save()
            engine=pyttsx3.init()
            engine.say(f"Thank you mr. {name}\n form submitted")
            engine.runAndWait()
            messages.success(request,"Form submitted")
            return redirect('contact_us')
    else:
        form=ContactForm
    return render(request,'contact/contact_us.html',{'form':form})



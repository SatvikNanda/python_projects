from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
# Create your views here.

def index(request):
    if request.method == "POST":
        form = ApplicationForm()
        
        first_name = form["first_name"]
        last_name = form["last_name"]
        email = form["email"]
        date = form["date"]
        occupation = form["occupation"]
            
        Form.objects.create(first_name=first_name, last_name=last_name, email=email, date=date, occupation=occupation)

        messages.success(request, "Form submitted successfully!")
    return render(request, "index.html")
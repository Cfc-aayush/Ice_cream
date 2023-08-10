from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages


# Create your views here.


def index(request):
    context = {
        'variable': "this is sent"
    }
    messages.success(request, "this is test message")
    return render(request, 'index.html', context)
    # return HttpResponse("This is homepage")


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        contact = Contact(name=name, email=email, phone=phone,
                          password=password, date=datetime.today())
        contact.save()  # Save the Contact object to the database

        # Provide a response to the user after saving the contact
        # return HttpResponse("Thanks for contacting us!")
        messages.success(request, "Profile details updated.")

    return render(request, 'contact.html')

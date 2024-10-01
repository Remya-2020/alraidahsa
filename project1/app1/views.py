import re
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib import messages
from app1.models import Contact

from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def mhome(request):
    return render(request,"home.html")

def about(request):
    return render(request,"aboutus.html")

def services(request):
    return render(request,"services.html")

def contactus(request):
    return render(request,"contactus.html")


@csrf_exempt
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        tel = request.POST.get('tel')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if not all([name, email, tel, subject, message]):
            messages.error(request, 'All fields are required.')

        if re.search(r'\D', tel):
            return render(request, "contact.html", {"error_message": "Enter valid numbers for 'tel'"})

        contact = Contact(name=name, email=email, tel=tel, subject=subject, message=message)
        contact.save()
        messages.success(request, 'Your message has been sent successfully!')

    return render(request, "contactus.html")
    #return HttpResponseRedirect(request.POST.get('next', '/'))




from django.shortcuts import render
from .models import Contact

# Create your views here.
def home(request):
    return render(request, 'page/Home.html')

def about(request):
    return render(request, 'page/About.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        return render(request, 'page/Thank.html')
    else:
        return render(request, 'page/Contact.html')
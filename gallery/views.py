from django.shortcuts import render

# Create your views here.
def baby(request):
    return render(request, 'gallery/Baby.html')

def product(request):
    return render(request, 'gallery/Product.html')

def country(request):
    return render(request, 'gallery/Country.html')
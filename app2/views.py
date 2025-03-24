from django.shortcuts import render

def contact(request):
    return render(request, 'contact.html')  # Using global template

def services(request):
    return render(request, 'services.html')  # Using global template


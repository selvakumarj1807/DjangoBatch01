from django.shortcuts import render

# Create your views here.

def index (request):
    return render (request, 'index.html')

def error (request):
    return render (request, '404.html')

def about (request):
    return render (request, 'about.html')

def appointment (request):
    return render (request, 'appointment.html')

def contact (request):
    return render (request, 'contact.html')

def department_details (request):
    return render (request, 'department-details.html')

def departments (request):
    return render (request, 'departments.html')

def doctor (request):
    return render (request, 'doctors.html')

def faq (request):
    return render (request, 'faq.html')

def gallery (request):
    return render (request, 'gallery.html')

def privacy (request):
    return render (request, 'privacy.html')

def service_details (request):
    return render (request, 'service-details.html')

def services (request):
    return render (request, 'services.html')

def starter_page (request):
    return render (request, 'starter-page.html')

def terms (request):
    return render (request, 'terms.html')

def testimonials (request):
    return render (request, 'testimonials.html')

from django.shortcuts import redirect, render

from app.forms import AppointmentForm
from app.models import Doctor

# Create your views here.

def index (request):
    return render (request, 'index.html')

def error (request):
    return render (request, '404.html')

def about (request):
    return render (request, 'about.html')


def appointment(request):
    form = AppointmentForm() 

    if request.method=='POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to the same view after successful form submission
    
    return render (request, 'appointment.html', {'form': form})

def contact (request):
    return render (request, 'contact.html')

def department_details (request):
    return render (request, 'department-details.html')

def departments (request):
    return render (request, 'departments.html')

def doctor (request):
    doctors = Doctor.objects.filter(status=False)
    context = {'doctors': doctors}
    return render (request, 'doctors.html', context)

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

from django import forms
from app.models import Appointment, Doctor

class AppointmentForm(forms.ModelForm):

    select_doctor = forms.ModelChoiceField(
        queryset=Doctor.objects.filter(status=False),
        empty_label="Choose Doctor",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    select_department = forms.ChoiceField(
        choices=[('', 'Choose Department')] +
        [(d, d) for d in Doctor.objects.values_list('Department_Name', flat=True).distinct()],
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Appointment
        fields = [
            'name', 'contact', 'email', 'date',
            'select_department', 'select_doctor', 'description'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'date': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
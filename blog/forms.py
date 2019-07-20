from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import Booking, Message


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'check_in': forms.TextInput(attrs={'class': 'form-control', 'id': 'checkin_date', 'placeholder': 'Check In'}),
            'check_out': forms.TextInput(attrs={'class': 'form-control', 'id': 'checkout_date', 'placeholder': 'Check Out'}),
            'adult': forms.Select(attrs={'class': 'form-control custom-select'}),
            'children': forms.Select(attrs={'class': 'form-control custom-select'}),
            'room_type': forms.Select(attrs={'class': 'form-control custom-select text-muted'})

        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control px-3 py-3', 'placeholder': 'Your Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control px-3 py-3', 'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control px-3 py-3', 'placeholder': 'Subject'}),
            'message': forms.TextInput(attrs={'class': 'form-control px-3 py-3', 'placeholder': 'Message'}),
        }

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Flight
from django.utils.safestring import mark_safe
from django.forms import widgets


class RegistrationForm(UserCreationForm):    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


from django import forms
from django.core.validators import MaxValueValidator
from .models import Flight

class FlightCreateForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['flight_number', 'departure_city', 'arrival_city', 'departure_date', 'arrival_date', 'price', 'seats_available']
        widgets = {
            'departure_date': forms.DateInput(format='%d-%m-%Y', attrs={'class': 'form-control'}),
            'arrival_date': forms.DateInput(format='%d-%m-%Y', attrs={'class': 'form-control'}),            
        }
        validators = {
            'price': [MaxValueValidator(999999.99)],
        }

    def __init__(self, *args, **kwargs):
        super(FlightCreateForm, self).__init__(*args, **kwargs)
        self.fields['departure_date'].input_formats = ['%d-%m-%Y']
        self.fields['arrival_date'].input_formats = ['%d-%m-%Y']
      



        """widgets = {
            'departure_city': forms.TextInput(attrs={'class': 'form-control'}),
            'arrival_city': forms.TextInput(attrs={'class': 'form-control'}),
            'departure_date': forms.DateInput(attrs={'class': 'form-control'}),
            'arrival_date': forms.DateInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'seats_available': forms.NumberInput(attrs={'class': 'form-control'}),
        }"""
        

"""
class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['departure_city', 'arrival_city','departure_time', 'arrival_time', 'price']
        widgets = {
            'departure_time': DateTimePicker(
                options={
                    'format': 'YYYY-MM-DD HH:mm',  # Specify the desired date and time format
                },
                attrs={
                    'placeholder': 'Select Departure Time',
                }
            ),
            'arrival_time': DateTimePicker(
                options={
                    'format': 'YYYY-MM-DD HH:mm',  # Specify the desired date and time format
                },
                attrs={
                    'placeholder': 'Select Arrival Time',
                }
            ),
        }
"""
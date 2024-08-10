# Dans forms.py de votre application Django

from django import forms
from .models import Property
from .models import Reservation 
from django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Cet email est déjà utilisé.")
        return email

class LoginForm(forms.Form):
    username = forms.CharField(label='Nom d\'utilisateur', max_length=100)
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)




class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control'})
        
        self.fields['old_password'].label = 'Current Password'
        self.fields['new_password1'].label = 'New Password'
        self.fields['new_password2'].label = 'Confirm New Password'
        
        self.fields['new_password1'].error_messages = {
            'required': 'Please enter a new password.',
            'password_mismatch': 'The two password fields didn’t match.',
            'password_too_similar': 'Your new password can’t be too similar to your personal information.',
            'password_too_short': 'Your new password must contain at least 8 characters.',
            'password_too_common': 'Your new password is too common.',
            'password_entirely_numeric': 'Your new password can’t be entirely numeric.',
        }
        self.fields['new_password2'].error_messages = {
            'required': 'Please confirm your new password.',
        }

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'city', 'address', 'price', 'bedrooms', 'bathrooms', 'description', 'image']

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'start_date', 'end_date', 'number_of_guests',
            'relationship', 'nationality', 'id_card_or_passport', 'guest_names'
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


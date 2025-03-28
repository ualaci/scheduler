from django import forms
from .models import Meeting,User,Location

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['date_time', 'requester', 'location' , 'purpose', 'coffe_service']
        labels = {
            'date_time': 'Data e Hora',
            'requester': 'Solicitante',
            'location': 'Local',
            'purpose': 'Finalidade',
            'coffee_service': 'Serviço de Copa',  
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'sector', 'phone', 'email']
        labels = {
            'name': 'Nome',
            'sector': 'Setor',
            'phone': 'Telefone',
            'email': 'Email'
        }

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name']
        labels = {'name': 'Local'}
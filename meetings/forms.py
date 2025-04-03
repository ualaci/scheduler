from django import forms
from .models import Meeting,User,Location
from django.core.exceptions import ValidationError
class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['date_time', 'date_time_end', 'requester', 'location' , 'purpose', 'coffe_service']
        labels = {
            'date_time': 'Data e Hora',
            'date_time_end': 'Data e Hora de Termino',
            'requester': 'Solicitante',
            'location': 'Local',
            'purpose': 'Finalidade',
            'coffee_service': 'Serviço de Copa',
        }

    #check meeting overlap
    def clean(self):
        cleaned_data = super().clean()
        date_time = cleaned_data.get("date_time")
        date_time_end = cleaned_data.get("date_time_end")
        location = cleaned_data.get("location")

        if date_time and date_time_end:
            overlapping_meetings = Meeting.objects.filter(
                location=location,
                date_time_end__gt=date_time,
                date_time__lt=date_time_end
            )

            if overlapping_meetings.exists():
                raise ValidationError("Erro: Já existe uma reunião agendada nesse horário para esse local.")

        return cleaned_data

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
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    sector = models.CharField(max_length=150)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.name} ({self.sector})"
    
class Location(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

class Meeting(models.Model):
    date_time = models.DateTimeField()
    requester = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    purpose = models.TextField()
    coffe_service = models.BooleanField(default=False)
    coffe_service_desc = models.TextField()


    def __str__(self):
        return (
            f"📅 {self.date_time.strftime('%d/%m/%Y %H:%M')}\n"
            f"🎯 Propósito: {self.purpose}\n"
            f"👤 Solicitado por: {self.requester}\n"
            f"📍 Local: {self.location}\n"
            f"☕ Serviço de Café: {'Sim' if self.coffe_service else 'Não'}"
        )

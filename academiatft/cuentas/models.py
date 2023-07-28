from django.db import models
def run():
    print("cuentas.models script is running!")

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
from django.db import models

class Spisok(models.Model):
    kartinka = models.ImageField(upload_to="images")
    name = models.CharField(max_length=20, blank=True, help_text='Введите имя объекта: ')
    summa = models.TextField(max_length=10, blank=True, help_text='Введите сумму: ')
    def __str__(self):
        return self.name

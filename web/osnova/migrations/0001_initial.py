# Generated by Django 5.0.1 on 2024-01-22 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='spisok',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kartinka', models.ImageField(upload_to='image/')),
                ('name', models.CharField(blank=True, help_text='Введите имя объекта: ', max_length=20)),
                ('summa', models.TextField(blank=True, help_text='Введите сумму: ', max_length=10)),
            ],
        ),
    ]

# Generated by Django 2.2.2 on 2020-01-30 15:25

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=20)),
                ('Date_Of_Birth', models.DateField()),
                ('Mobile_Number', phone_field.models.PhoneField(help_text='Contact Phone NUmber', max_length=31)),
            ],
        ),
    ]

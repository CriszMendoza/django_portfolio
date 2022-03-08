from distutils.command.upload import upload
from email.mime import image
from turtle import title
from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField


class Proyect(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=100)
    image = ImageField(upload_to='portfolio/images')
    url = URLField(blank=True)

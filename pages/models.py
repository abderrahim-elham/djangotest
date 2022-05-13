from distutils.command.upload import upload
from django.db import models
from django.forms import FilePathField
import os

# Create your models here.

class Etudiant(models.Model):
      username=models.CharField(max_length=100)
      password=models.CharField(max_length=100)
      indenti=models.CharField(max_length=100)
      image=models.ImageField(upload_to='imagesUser/', default=None)
      def __str__(self):
        return self.username
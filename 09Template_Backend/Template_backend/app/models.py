# Create your models here.
from datetime import datetime
import os
from django.db import models

# Create your models here.


def getFileName(request, filename):
    now_time = datetime.now().strftime("%Y%m%d%H%M%S")
    new_filename = f"{now_time}_{filename}" 
    return os.path.join('doctorIMG', new_filename)

class Doctor(models.Model):
    Doctor_name = models.CharField(max_length=100)
    Experience = models.CharField(max_length=100)
    Department_Name = models.CharField(max_length=15)
    Description = models.TextField()
    image = models.ImageField(upload_to= getFileName, null=True, blank=True)
    status = models.BooleanField(default=False, help_text="0:Show, 1:Hidden")
    specialist = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Doctor_name
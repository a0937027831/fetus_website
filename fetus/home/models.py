import uuid
import os
from django.db import models
from django_cleanup import cleanup

def image_file_path(instance,filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join('uploads/banner/',filename)

class Banner(models.Model):
    image1 = models.ImageField(upload_to = image_file_path,blank=True,default='',help_text='封面1 寬:450px 高:450px')
    image2 = models.ImageField(upload_to = image_file_path,blank=True,default='',help_text='封面2 寬:450px 高:450px')
    image3 = models.ImageField(upload_to = image_file_path,blank=True,default='',help_text='封面3 寬:450px 高:450px')
    image4 = models.ImageField(upload_to = image_file_path,blank=True,default='',help_text='封面4 寬:450px 高:450px')
    image5 = models.ImageField(upload_to = image_file_path,blank=True,default='',help_text='封面5 寬:450px 高:450px')



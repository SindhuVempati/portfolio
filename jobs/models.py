from django.db import models
#to save this in database
class Job(models.Model):
    image = models.ImageField(upload_to = 'images/')
    summary = models.CharField(max_length=200)

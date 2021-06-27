from django.db import models

# Create your models here.

class Data(models.Model):

    timestamp = models.CharField(unique=True, max_length=256)
    bpm = models.FloatField()
    spO2 = models.FloatField()

    def __str__(self):
        return self.timestamp
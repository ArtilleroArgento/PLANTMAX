from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    care = models.TextField()

    def __str__(self):
        return self.name



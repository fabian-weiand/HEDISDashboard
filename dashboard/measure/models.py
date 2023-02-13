from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Measure(models.Model):
    title = models.CharField(max_length=100)
    acronym = models.CharField(max_length=100)
    description = models.TextField()
    measure_year = models.IntegerField()
    population = models.TextField()
    exclusions = models.TextField()
    denominator = models.TextField()
    numerator = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
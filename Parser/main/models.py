from django.db import models

from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    salary = models.CharField(max_length=255, null=True, blank=True)
    link = models.URLField()

    def str(self):
        return self.title

class Anketa(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    skills = models.TextField()
    link = models.URLField()

    def str(self):
        return self.name

from django.db import models

# Create your models here.
class Students(models.Model):
	std_id = models.IntegerField()
	Name = models.CharField(max_length=255)
	Course = models.CharField(max_length=255)
	email = models.EmailField()
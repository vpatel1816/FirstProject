from django.db import models

# Create your models here.
class Info(models.Model):
	Name = models.CharField(max_length=20)
	Eid = models.CharField(max_length=8)
	Contact = models.IntegerField()
	Address = models.CharField(max_length=100)

	def __str__(self):
		return self.Name
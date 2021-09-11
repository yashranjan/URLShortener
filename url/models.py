from djongo import models

# Create your models here.
class URLField(models.Model):
	originalURL = models.CharField(max_length=300)
	shortURL = models.CharField(max_length=100,unique=True)

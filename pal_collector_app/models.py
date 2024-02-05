from django.db import models

# Create your models here.
class Pals(models.Model):
  name = models.CharField(max_length=120)

  def __str__(self):
    return self.name

class Weapons(models.Model):
  name = models.CharField(max_length=4)
  pal = models.ManyToManyField(Pals)

  def __str__(self):
    return f"{self.name}"
from django.db import models

# Create your models here.
class Pals(models.Model):
    name = models.CharField(max_length=50, default="")
    pal_number = models.CharField(max_length=6, default="")
    element_1 = models.CharField(max_length=20, default="")
    element_2 = models.CharField(max_length=20, default="")
    food = models.IntegerField(default=0)

    def __str__(self):
        return self.pal_number

class Weapons(models.Model):
    name = models.CharField(max_length=4)
    weapon_number = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"
    
class Work_traits(models.Model):
    pal_number = models.CharField(max_length=6, default="")
    kindling = models.IntegerField(default=0)
    planting = models.IntegerField(default=0)
    handiwork = models.IntegerField(default=0)
    lumbering = models.IntegerField(default=0)
    medicine = models.IntegerField(default=0)
    transporting = models.IntegerField(default=0)
    watering = models.IntegerField(default=0)
    generating = models.IntegerField(default=0)
    gathering = models.IntegerField(default=0)
    mining = models.IntegerField(default=0)
    cooling = models.IntegerField(default=0)
    farming = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.pal_number}"

class My_pals(models.Model):
    given_name = models.CharField(max_length=60, default="")
    pal_number = models.CharField(max_length=6, default="")
    weapon = models.ManyToManyField(Weapons)

    def __str__(self):
        return f"{self.pal_number}"
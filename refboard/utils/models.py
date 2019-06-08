from django.db import models
from django.utils import timezone


class RefMaterial(models.Model):
    name = models.CharField("name", max_length=255)
    filename = models.CharField("filename", max_length=255)

    def __str__(self):
        return self.name


class Thing(models.Model):
    name = models.CharField("name", max_length=255)
    client = models.CharField("client", max_length=255)
    init_date = models.DateTimeField("init date", default=timezone.now)

    def __str__(self):
        return self.name


class Thingy(models.Model):
    name = models.CharField("name", max_length=255)
    thing = models.ForeignKey(Thing, on_delete=models.CASCADE, related_name="things")
    ref_materials = models.ManyToManyField(RefMaterial, related_name="ref_materials")

    def __str__(self):
        return self.name


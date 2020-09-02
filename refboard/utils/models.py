from django.db import models
from django.utils import timezone

MATERIAL_TYPE = ( 
    ("image", "image"), 
    ("video", "video"), 
    ("website", "website")
) 


class RefMaterial(models.Model):
    name = models.CharField("name", max_length=255)
    filename = models.CharField("filename", max_length=255)
    thumbnail = models.CharField("thumbnail", max_length=255)
    medium = models.CharField("medium", max_length=255)
    m_type = models.CharField( 
        max_length = 20, 
        choices = MATERIAL_TYPE, 
        default = 'image'
        )

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


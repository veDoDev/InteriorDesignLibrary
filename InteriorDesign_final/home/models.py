from django.db import models

# Create your models here.
class ProjectData(models.Model):
    title = models.CharField(max_length=255)
    Dimentions = models.TextField(default="Default Dimentions")
    RoomHighlights = models.TextField(default="Standard Room")
    RoomType = models.TextField(default = "Uspecified")
    FurnitureHighlights = models.TextField(default = "Standard Furniture")
    image = models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.title
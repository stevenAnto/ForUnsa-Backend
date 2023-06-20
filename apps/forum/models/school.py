from django.db import models
from . import Base

class School(Base):
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length=64, unique=True) # slug for links
    
    class Meta:
        ordering = ['name']
    
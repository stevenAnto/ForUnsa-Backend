from django.db import models
from django.utils.text import slugify
from . import Base

class Tag(Base):
    name = models.CharField(max_length=32, unique=True)
    slug = models.SlugField(max_length=32, unique=True, editable=False) # slug for links
    
    class Meta:
        ordering = ['name']
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)
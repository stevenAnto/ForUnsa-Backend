from django.db import models
from django.utils.text import slugify
from . import Base
from .section import Section

class School(Base):
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length=64, unique=True, editable=False) # slug for links

    class Meta:
        ordering = ['name']

    def get_default_school():
        return School.objects.get_or_create(name='Not defined school')[0]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(School, self).save(*args, **kwargs)
        section, created = Section.objects.get_or_create(slug=self.slug)
        if created:
            section.name = self.name
            section.save()

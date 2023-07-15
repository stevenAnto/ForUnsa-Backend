from django.db import models
from django.utils.text import slugify
from . import Base

class Section(Base):
    name = models.CharField(max_length=64, unique=True)
    posts_count = models.BigIntegerField(default=0)
    slug = models.SlugField(max_length=64, unique=True, editable=False) # slug for links
    
    class Meta:
        ordering = ['name']
        
    def get_default_section():
        return Section.objects.get_or_create(name='No Section')[0]
    
    def get_custom_section(user):
        if not hasattr(user, 'current_school'):
            return None
        sections = user.school.section_set.all()
        if sections.exists():
            return sections.first()
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Section, self).save(*args, **kwargs)
    
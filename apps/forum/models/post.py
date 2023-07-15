from django.db import models
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator
from apps.forum.validators import MaxWeightValidator
from . import Base, Tag, Section
from .post_base import PostBase

class PostType(Base):
    name = models.CharField(max_length=64, unique=True) # I mean is a question or advice or general information
    
    class Meta:
        ordering = ['name']
        
    def get_default_type():
        return PostType.objects.get_or_create(name='Social', id='1')[0].id
    
class ApprovalStatus(Base):
    name = models.CharField(max_length=64, unique=True)
    
    class Meta:
        ordering = ['name']
        
    def get_default_status():
        return ApprovalStatus.objects.get_or_create(name='Default status', id=10)[0].id
    

class Post(PostBase):
    title = models.CharField(max_length=128)
    content = models.TextField(max_length=255, blank=True)
    img = models.ImageField(upload_to='posts', blank=True, validators=[MaxWeightValidator(2)])
    file = models.FileField(upload_to='posts', blank=True, validators=[FileExtensionValidator(['pdf', 'doc','docx'])])
    tags = models.ManyToManyField(Tag, blank=True)
    section = models.ForeignKey(Section, on_delete=models.SET(Section.get_default_section), default=Section.get_custom_section(PostBase.user)) # If deleted section, then set default
    post_type = models.ForeignKey(PostType, on_delete=models.SET_DEFAULT, default=PostType.get_default_type) # To MODIFY in MODEL, if is a blbliography resource or question(like social), etc
    approval_status = models.ForeignKey(ApprovalStatus, on_delete=models.SET_DEFAULT, default=ApprovalStatus.get_default_status)
    slug = models.SlugField(max_length=64, editable=False) # slug for links
    
    class Meta:
        ordering = ['-likes_count']
        
    def save(self, *args, **kwargs):
            
        self.slug = slugify(self.title)
        # if have value on img then save with post type social if have value on file then save with post type bibliograpy resource, if don't value on both then social post type
        self.post_type = PostType.objects.get_or_create(name='Social')[0]
        if self.file:
            self.post_type = PostType.objects.get_or_create(name='Bibliography resource')[0]
        if not self.pk:
            self.section.posts_count += 1
            self.section.save()
        super(Post, self).save(*args, **kwargs)
    
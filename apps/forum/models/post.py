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
        return PostType.objects.get_or_create(name='Default type')[0].id
    
class ApprovalStatus(Base):
    name = models.CharField(max_length=64, unique=True)
    
    class Meta:
        ordering = ['name']
        
    def get_default_status():
        return ApprovalStatus.objects.get_or_create(name='Default status', id=10)[0].id
    

class Post(PostBase):
    title = models.CharField(max_length=128)
    content = models.TextField(max_length=255, blank=True)
    img = models.ImageField(upload_to='posts', blank=True, validators=[MaxWeightValidator])
    file = models.FileField(upload_to='posts', blank=True, validators=[FileExtensionValidator(['pdf', 'doc','docx'])])
    tags = models.ManyToManyField(Tag, blank=True)
    section = models.ForeignKey(Section, on_delete=models.SET_DEFAULT, default=Section.get_default_section) # If deleted section, then set default
    post_type = models.ForeignKey(PostType, on_delete=models.SET_DEFAULT, default=PostType.get_default_type) # To MODIFY in MODEL, if is a question or advice, etc
    approval_status = models.ForeignKey(ApprovalStatus, on_delete=models.SET_DEFAULT, default=ApprovalStatus.get_default_status)
    likes_count = models.BigIntegerField(default=0)
    dislikes_count = models.BigIntegerField(default=0)
    slug = models.SlugField(max_length=64, unique=True, editable=False) # slug for links
    
    class Meta:
        ordering = ['-likes_count']
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
    
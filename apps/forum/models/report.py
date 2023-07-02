from django.db import models
from django.contrib.auth.models import User
from . import Base
from .post import PostBase

class Report(Base):
    post = models.ForeignKey(PostBase, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    information = models.TextField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
    # slug = models.SlugField(max_length=64, unique=True) # slug for links, removed for requirements
    
    class Meta:
        ordering = ['-post']
        
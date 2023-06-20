from django.db import models
from django.contrib.auth.models import User
from . import Base, PostBase

class SavePost(Base):
    post = models.ForeignKey(PostBase, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # slug = models.SlugField(max_length=64, unique=True) # slug for links, removed for requirements, this seems uncompleted
    
    class Meta:
        ordering = ['-post']
        
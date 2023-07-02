from django.db import models
from . import Base
from .post import PostBase

class Comment(PostBase, Base):
    posted_on = models.ForeignKey(PostBase, related_name='posted_on_%(class)s', on_delete=models.CASCADE) # it should be consider another comment too
    content = models.TextField(max_length=255)
    likes_count = models.BigIntegerField(default=0)
    dislikes_count = models.BigIntegerField(default=0)
    # slug = models.SlugField(max_length=64, unique=True) # slug for links, removed seems unnecessary
    
    class Meta:
        ordering = ['-likes_count']
    
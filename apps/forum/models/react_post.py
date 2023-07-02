from django.db import models
from django.contrib.auth.models import User
from . import Base
from .post import PostBase
from .reaction import Reaction

class ReactPost(Base):
    post = models.ForeignKey(PostBase, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_reaction = models.ForeignKey(Reaction, on_delete=models.SET(Reaction.get_default_reaction))
    made_at = models.DateTimeField(auto_now_add=True) 
    
    class Meta:
        ordering = ['-post']
        unique_together = ('post', 'user')
        
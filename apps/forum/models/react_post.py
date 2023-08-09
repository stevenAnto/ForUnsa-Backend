from django.db import models
from django.db import IntegrityError
from django.contrib.auth.models import User
from . import Base
from .post import PostBase
from .reaction import Reaction

class ReactPost(Base):
    post = models.ForeignKey(PostBase, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_reaction = models.ForeignKey(Reaction, on_delete=models.SET(Reaction.get_default_reaction))
    made_at = models.DateTimeField(auto_now=True) 
    
    class Meta:
        ordering = ['-post']
        # a way to define that a user can react to certainn post with only one reaction
        unique_together = ('post', 'user')
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.add_reacts()
        elif self.state == 'X':
            self.remove_reacts()
        try:
            super(ReactPost, self).save(*args, **kwargs)
        except IntegrityError as e:
            if 'unique constraint' in str(e).lower():
                # handle the unique constraint violation
                existing_instance = ReactPost.objects.get(post=self.post, user=self.user)
                existing_instance.post_reaction = self.post_reaction
                self.remove_reacts(self)
                existing_instance.save()
            else:
                raise e
    
    def add_reacts(self):
        if self.post_reaction.description == "Like reaction":
            self.post.likes_count += 1
            self.post.save()
        
        if self.post_reaction.description == "Dislike reaction":
            self.post.dislikes_count += 1
            self.post.save()
    
    def remove_reacts(self):
        if self.post_reaction.description == "Like reaction":
            self.post.dislikes_count -= 1
            self.post.likes_count += 1
            self.post.save()
        
        if self.post_reaction.description == "Dislike reaction":
            self.post.likes_count -= 1
            self.post.dislikes_count += 1
            self.post.save()
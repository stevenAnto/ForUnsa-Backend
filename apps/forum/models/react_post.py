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
        if self.pk is None:
            # Instance does not exist yet
            self.reacts(self, self.post_reaction, 1)
        else:
            original_instance = ReactPost.objects.get(pk=self.pk)

            if original_instance.state == 'A' and self.state == 'X':
                self.reacts(self, original_instance.post_reaction, -1)
            if original_instance.state == 'X' and self.state == 'A':
                self.reacts(self, self.post_reaction, 1)

            if original_instance.post_reaction.description != self.post_reaction.description:
                self.reacts(self, original_instance.post_reaction, -1)
                self.reacts(self, self.post_reaction, 1)

            if original_instance.post != self.post:
                self.reacts(original_instance, original_instance.post_reaction, -1)
                self.reacts(self, self.post_reaction, 1)
                
        super().save(*args, **kwargs)
            
    @staticmethod         
    def reacts(self, reaction, amount):
        if reaction.description == "Like reaction":
            self.post.likes_count += amount

        if reaction.description == "Dislike reaction":
            self.post.dislikes_count += amount

        self.post.save()

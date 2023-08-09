from django.db import models
from .post_base import PostBase

class Comment(PostBase):
    posted_on = models.ForeignKey(PostBase, related_name='posted_on_%(class)s', on_delete=models.CASCADE) # it should be consider another comment too
    content = models.TextField(max_length=255)
    # slug = models.SlugField(max_length=64, unique=True) # slug for links, removed seems unnecessary
    
    class Meta:
        ordering = ['-likes_count']
    
    def save(self, *args, **kwargs):
        instance = self
        try:
            original_instance = Comment.objects.get(pk=instance.pk)
        except Comment.DoesNotExist:
            # Instance does not exist yet
            # self.section = self.posted_on.section
            self.posted_on.comments_count += 1
            self.posted_on.save()
            
            super().save()
            return

        if original_instance.state == 'A':
            if instance.state == 'X':
                self.posted_on.comments_count -= 1
        if original_instance.state == 'X':
            if instance.state == 'A':
                self.posted_on.comments_count += 1
                
        super(Comment, self).save(*args, **kwargs)
    
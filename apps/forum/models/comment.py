from django.db import models
from .post import PostBase

class Comment(PostBase):
    posted_on = models.ForeignKey(PostBase, related_name='posted_on_%(class)s', on_delete=models.CASCADE) # it should be consider another comment too
    content = models.TextField(max_length=255)
    # slug = models.SlugField(max_length=64, unique=True) # slug for links, removed seems unnecessary
    
    class Meta:
        ordering = ['-likes_count']
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.posted_on.comments_count += 1
            self.posted_on.save()
        super(Comment, self).save(*args, **kwargs)
    
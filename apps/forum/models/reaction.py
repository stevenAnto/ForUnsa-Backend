from django.db import models
from . import Base

class Reaction(Base):
    description = models.CharField(max_length=255, unique=True)
    
    def get_default_reaction():
        # Creating the like and dislike items
        Reaction.objects.get_or_create(description="Like reaction", id=1)[0]
        Reaction.objects.get_or_create(description="Dislike reaction", id=2)[0]
        return Reaction.objects.get_or_create(description="Default reaction", id=10)[0]
    
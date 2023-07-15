from django.db import models
from django.contrib.auth.models import User
from . import Base
from .custom_user import CustomUser

class PostBase(Base):
    user = models.ForeignKey(User, on_delete=models.SET(CustomUser.get_deleted_user)) # if User deleted set certain User
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes_count = models.BigIntegerField(default=0, editable=False)
    dislikes_count = models.BigIntegerField(default=0, editable=False)
    comments_count = models.BigIntegerField(default=0, editable=False)
    
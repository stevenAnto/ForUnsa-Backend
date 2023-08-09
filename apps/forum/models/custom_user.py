from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from apps.forum.validators import MaxWeightValidator
from . import Base, School

class CustomUser(User, Base):
    # id, name, last_name, email, nickname, is_admin, is_staff included on User
    current_school = models.ForeignKey(School, on_delete=models.SET(School.get_default_school), default=School.get_default_school)  # School of the user e.g. System Engineering
    biography = models.CharField(max_length=255, blank=True)  # description of user
    img = models.ImageField(upload_to='profiles', default='profiles/default.jpg', validators=[MaxWeightValidator(2)])
    is_featured = models.BooleanField(default=False)  # user is featured
    semester = models.CharField(max_length=32, default='not defined')  # inital semester
    registration_code = models.CharField(max_length=8, blank=True, null=True)
    registration_completed = models.BooleanField(default=False)
    slug = models.SlugField(max_length=64, unique=True,editable=False)  # slug for links
    is_logued = models.BooleanField(default=False)  # user is logued

    def get_deleted_user():
        return CustomUser.objects.get_or_create(username="Deleted", )[0]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(User, self).save(*args, **kwargs)

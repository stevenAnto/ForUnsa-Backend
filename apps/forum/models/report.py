from django.db import models
from django.contrib.auth.models import User
from . import Base
from .post import PostBase

class ReportType(Base):
    name = models.CharField(max_length=64, unique=True) # kinda fake information
    
    class Meta:
        ordering = ['name']
        
    def get_default_type():
        return ReportType.objects.get_or_create(name="Default report type", id="1")[0]

class Report(Base):
    post = models.ForeignKey(PostBase, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    information = models.TextField(max_length=1024)
    report_tyoe = models.ForeignKey(ReportType, on_delete=models.SET_DEFAULT, default=ReportType.get_default_type)
    created_at = models.DateTimeField(auto_now_add=True)
    # slug = models.SlugField(max_length=64, unique=True) # slug for links, removed for requirements
    
    class Meta:
        ordering = ['-post']
        
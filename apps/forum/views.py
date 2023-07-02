from rest_framework import viewsets
from .models.comment import Comment
from .models.custom_user import CustomUser
from .models.post import Post
from .models.react_post import ReactPost
from .models.reaction import Reaction
from .models.report import Report 
from .models.save_post import SavePost
from .models.school import School
from .models.section import Section
from .models.tag import Tag
from .serializers import CommentSerializer, CustomUserSerializer, PostSerializer, ReactPostSerializer, ReactionSerializer, ReportSerializer, SavePostSerializer, SchoolSerializer, SectionSerializer, TagSerializer

# Create your views here.
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class ReacPostViewSet(viewsets.ModelViewSet):
    queryset = ReactPost.objects.all()
    serializer_class = ReactPostSerializer
    
class ReactionViewSet(viewsets.ModelViewSet):
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer
    
class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    
class SavePostViewSet(viewsets.ModelViewSet):
    queryset = SavePost.objects.all()
    serializer_class = SavePostSerializer

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

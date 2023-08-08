from rest_framework import viewsets
from .models.comment import Comment
from .models.custom_user import CustomUser
from .models.post import Post, PostType, ApprovalStatus
from .models.react_post import ReactPost
from .models.reaction import Reaction
from .models.report import Report, ReportType
from .models.save_post import SavePost
from .models.school import School
from .models.section import Section
from .models.tag import Tag
from .serializers import CommentSerializer, CustomUserSerializer, PostSerializer, PostTypeSerializer, ApprovalStatusSerializer, ReactPostSerializer, ReactionSerializer, ReportSerializer, ReportTypeSerializer, SavePostSerializer, SchoolSerializer, SectionSerializer, TagSerializer
from django.core.mail import send_mail
from django.http import JsonResponse
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.views.decorators.csrf import csrf_exempt
import json

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

class PostTypeViewSet(viewsets.ModelViewSet):
    queryset = PostType.objects.all()
    serializer_class = PostTypeSerializer

class ApprovalStatusViewSet(viewsets.ModelViewSet):
    queryset = ApprovalStatus.objects.all()
    serializer_class = ApprovalStatusSerializer    
    
class ReacPostViewSet(viewsets.ModelViewSet):
    queryset = ReactPost.objects.all()
    serializer_class = ReactPostSerializer
    
class ReactionViewSet(viewsets.ModelViewSet):
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer
    
class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class ReportTypeViewSet(viewsets.ModelViewSet):
    queryset = ReportType.objects.all()
    serializer_class = ReportTypeSerializer
        
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

@csrf_exempt
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def email(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        recipient = data.get('recipient')
        subject = data.get('subject')
        message = data.get('message')
        try:
            send_mail(subject, message, 'forunsaapp@gmail.com', [recipient])
            return JsonResponse({'message': 'Email sent successfully.'})
        except Exception as e:
            return JsonResponse({'message': f'Error: {str(e)}'}, status=500)

    return JsonResponse({'message': 'Invalid request method.'}, status=400)
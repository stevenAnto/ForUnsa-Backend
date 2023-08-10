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
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import random
import string
from postmarker.core import PostmarkClient

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


@api_view(['POST'])
def login_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        print(email)
        print(password)
        try:
            user = CustomUser.objects.get(email=email, password=password)
            user.is_logued = True
            user.save()
            print("---> IMPRIMIENDO" + user.id )
            return Response({'id': user.id})
        except CustomUser.DoesNotExist:
            return Response({'message': 'Invalid email or password.'}, status=400)

@api_view(['POST'])
def register_user(request):
    email = json.loads(request.body).get('email')
    if CustomUser.objects.filter(email=email).first() is not None:
        return Response({'is_email': 1})
    else: 
        serializer = CustomUserSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            user = serializer.save()
            # Generate and assign a registration code
            registration_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            user.registration_code = registration_code
            user.save()
            # Email
            postmark = PostmarkClient(server_token='e937776b-95a8-4a60-be94-e9c1373aee3f')
            postmark.emails.send(
                From='bhanccoco@unsa.edu.pe',
                To=user.email,
                Subject='Registro Exitoso',
                HtmlBody="Hola {}, ¡Bienvenido a la comunidad de ForUnsa!\nCódigo de Verificación: {}".format(user.username,registration_code)
            )
            """recipient = user.email
            subject = "Registro Exitoso"
            message = "Hola {}, ¡Bienvenido a la comunidad de ForUnsa!\nCódigo de Verificación: {}".format(user.username,registration_code)
            send_mail(subject, message, 'forunsaapp@gmail.com', [recipient])"""
            return Response({'is_email': 0})
        return Response(serializer.errors, status=400)

@api_view(['POST'])
def complete_registration(request):
    data = json.loads(request.body)
    email = data.get('email')
    registration_code = data.get('registrationCode')

    try:
        user = CustomUser.objects.get(email=email, registration_code=registration_code)
        user.registration_completed = True
        user.save()
        return Response({'message': 'Registration completed successfully.'})
    except CustomUser.DoesNotExist:
        return Response({'message': 'Invalid email or registration code.'}, status=400)

"""@csrf_exempt
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

    return JsonResponse({'message': 'Invalid request method.'}, status=400)"""

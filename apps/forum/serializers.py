from rest_framework import serializers
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

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        
class PostTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostType
        fields = '__all__'

class ApprovalStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApprovalStatus
        fields = '__all__'

class ReactPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReactPost
        fields = '__all__'

class ReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
        
class ReportTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportType
        fields = '__all__'

class SavePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavePost
        fields = '__all__'

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'
    
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
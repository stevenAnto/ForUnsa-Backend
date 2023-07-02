from django.urls import path, include
from rest_framework import routers
from .views import CommentViewSet, CustomUserViewSet, PostViewSet, ReacPostViewSet, ReactionViewSet, ReportViewSet, SavePostViewSet, SchoolViewSet, SectionViewSet, TagViewSet

router = routers.DefaultRouter()
router.register(r'comment', CommentViewSet, 'comment')
router.register(r'custom_user', CustomUserViewSet, 'custom_user')
router.register(r'post', PostViewSet, 'post')
router.register(r'react_post', ReacPostViewSet, 'react_post')
router.register(r'reaction', ReactionViewSet, 'reaction')
router.register(r'report', ReportViewSet, 'report')
router.register(r'save_post', SavePostViewSet, 'save_post')
router.register(r'school', SchoolViewSet, 'school')
router.register(r'section', SectionViewSet, 'section')
router.register(r'tag', TagViewSet, 'tag')

urlpatterns = [
    path('', include(router.urls))
]
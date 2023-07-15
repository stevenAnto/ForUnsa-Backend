from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from .views import CommentViewSet, CustomUserViewSet, PostViewSet, PostTypeViewSet, ApprovalStatusViewSet, ReacPostViewSet, ReactionViewSet, ReportViewSet, ReportTypeViewSet, SavePostViewSet, SchoolViewSet, SectionViewSet, TagViewSet

router = routers.DefaultRouter()
router.register(r'comment', CommentViewSet, 'comment')
router.register(r'user', CustomUserViewSet, 'custom_user')
router.register(r'post', PostViewSet, 'post')
router.register(r'post_type', PostTypeViewSet, 'post_type')
router.register(r'approval_status', ApprovalStatusViewSet, 'approval_status')
router.register(r'react_post', ReacPostViewSet, 'react_post')
router.register(r'reaction', ReactionViewSet, 'reaction')
router.register(r'report', ReportViewSet, 'report')
router.register(r'report_type', ReportTypeViewSet, 'report_type')
router.register(r'save_post', SavePostViewSet, 'save_post')
router.register(r'school', SchoolViewSet, 'school')
router.register(r'section', SectionViewSet, 'section')
router.register(r'tag', TagViewSet, 'tag')

urlpatterns = [
    path('', include(router.urls)),
    # path('api/v1/', include(router.urls)), # Api versioning rules
    path('docs/', include_docs_urls(title='ForUnsa documentation')),
]
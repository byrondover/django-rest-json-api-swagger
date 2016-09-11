from django.conf.urls import include, url
from rest_framework import routers

from example.views import BlogViewSet, EntryViewSet, AuthorViewSet, CommentViewSet, schema_view

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'blogs', BlogViewSet)
router.register(r'entries', EntryViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-docs', schema_view),
]

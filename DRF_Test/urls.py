from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from social.api.viewsets import CommentsViewSet, RepliesViewSet

router = routers.DefaultRouter()
router.register(r'comments', CommentsViewSet)
router.register(r'replies', RepliesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

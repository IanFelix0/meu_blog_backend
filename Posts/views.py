from rest_framework import viewsets
from .serializer import PostSerializer
from .models import Post
from rest_framework.permissions import IsAuthenticated

class PostListView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
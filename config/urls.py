from django.contrib import admin
from django.urls import path, include,re_path

from rest_framework import routers

from django.conf.urls.static import static
from django.conf import settings

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

from Posts import views

from django.views.generic import TemplateView

route = routers.DefaultRouter()

route.register(r'posts', views.PostListView, basename='Posts')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/',TokenObtainPairView.as_view()),
    path('token/refresh',TokenRefreshView.as_view()),
    path('blog/', include(route.urls)),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns += [re_path(r'^.*',TemplateView.as_view(template_name='index.html'))]

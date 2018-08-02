from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'post', api.PostViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Post
    path('app_name/post/', views.PostListView.as_view(), name='app_name_post_list'),
    path('app_name/post/create/', views.PostCreateView.as_view(), name='app_name_post_create'),
    path('app_name/post/detail/<int:pk>/', views.PostDetailView.as_view(), name='app_name_post_detail'),
    path('app_name/post/update/<int:pk>/', views.PostUpdateView.as_view(), name='app_name_post_update'),
)
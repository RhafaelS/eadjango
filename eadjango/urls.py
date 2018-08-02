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
    path('eadjango/post/', views.PostListView.as_view(), name='eadjango_post_list'),
    path('eadjango/post/create/', views.PostCreateView.as_view(), name='eadjango_post_create'),
    path('eadjango/post/detail/<int:pk>/', views.PostDetailView.as_view(), name='eadjango_post_detail'),
    path('eadjango/post/update/<int:pk>/', views.PostUpdateView.as_view(), name='eadjango_post_update'),
)
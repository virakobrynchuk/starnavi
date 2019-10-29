from django.urls import path, include
from .views import PostListView, PostCreateView
from . import views


urlpatterns = [
    path('view_posts/', PostListView.as_view(), name='Posts'),
    path('create/', PostCreateView.as_view(), name='CreatePost'),
    path('like/<pk>/', views.like_post, name='LikePost'),
    path('unlike/<pk>/', views.unlike_post, name='UnlikePost'),
]
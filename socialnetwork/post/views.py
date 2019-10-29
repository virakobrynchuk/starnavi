from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Post, Like

from . import serializers
from rest_framework import generics


class ListOfPosts(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.TodoSerializer


class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.TodoSerializer


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'post/view_posts.html'
    context_object_name = 'latest_posts'
    ordering = ['-pub_date']
    paginate_by = 3


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['post_title', 'post_text']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


@login_required()
def like_post(request, pk):
    post_liked = get_object_or_404(Post, pub_date=pk)
    try:
        obj = Like.objects.get(like_user=request.user, like_post=post_liked)
        return redirect('Posts')
    except Like.DoesNotExist:
        new_like = Like()
        new_like.like_user = request.user
        new_like.like_post = post_liked
        new_like.like_value = 1
        post_liked.post_likes += 1
        new_like.save()
        post_liked.save()
        return redirect('Posts')


@login_required()
def unlike_post(request, pk):
    post_liked = get_object_or_404(Post, pub_date=pk)
    try:
        obj = Like.objects.get(like_user=request.user, like_post=post_liked)
        obj.delete()
        post_liked.post_likes -= 1
        post_liked.save()
        return redirect('Posts')
    except Like.DoesNotExist:
        return redirect('Posts')


def is_user_auth(request):
    current_user = str(request.user.is_authenticated)
    current_username = str(request.user)

    result = '<p> ' + current_user + ' </p> <p> Name: ' + current_username + '</p>'

    return HttpResponse(result)



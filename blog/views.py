from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Post
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        posts = super().get_queryset()
        #postsを降順に並び替える
        return posts.order_by('-updated_at')

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_object(self, queryset=None):
        post = super().get_object(queryset)
        #公開済みorログイン時にアクセス可能
        if post.is_published or self.request.user.is_authenticated:
            return post
        else:
            return Http404
        
class CategoryPostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"

    def get_queryset(self):
        
        return super().get_queryset()
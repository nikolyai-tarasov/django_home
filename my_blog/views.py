from django.urls import reverse_lazy

from my_blog.models import Post
from django.views.generic import ListView, DetailView, UpdateView


class HomeView(ListView):
    model = Post
    template_name = 'home_blog.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    success_url = reverse_lazy('my_blog: home_blog')

class ReformPostViews(UpdateView):
    model = Post
    fields = ['heading', 'created_at', 'description', 'image']
    template_name = 'reform_post.html'
    success_url = reverse_lazy('my_blog: home_blog')






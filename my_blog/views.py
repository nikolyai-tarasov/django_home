from django.urls import reverse_lazy

from my_blog.models import Post
from django.views.generic import ListView, DetailView, UpdateView


class HomeView(ListView):
    model = Post
    template_name = 'home_blog.html'
    context_object_name = 'posts'
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(publication=True)


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    success_url = reverse_lazy('my_blog: home_blog')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ReformPostViews(UpdateView):
    model = Post
    fields = ['heading', 'created_at', 'description', 'image']
    template_name = 'reform_post.html'
    success_url = reverse_lazy('my_blog:home_blog')

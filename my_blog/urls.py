from django.urls import path
from my_blog.apps import MyBlogConfig
from my_blog.views import HomeView, PostDetailView, ReformPostViews

app_name = MyBlogConfig.name

urlpatterns = [
    path('home_blog/', HomeView.as_view(), name="home_blog"),
    path('post_detail/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('reform_post/<int:pk>/', ReformPostViews.as_view(), name='reform_post'),

]

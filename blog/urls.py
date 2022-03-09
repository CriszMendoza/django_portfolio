from django.urls import path
from .views import render_posts, render_post_detail


app_name = 'blog'

urlpatterns = [
    path('', render_posts, name='posts'),
    path('/post/<int:post_id>', render_post_detail, name='post_detail')
]

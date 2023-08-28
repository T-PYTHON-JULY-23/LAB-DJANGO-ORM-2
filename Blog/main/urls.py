from django.urls import path
from . import views

app_name="main"

urlpatterns = [
    path('', views.blog_view, name='blog_view'),
    path('addPost/', views.add_post_view, name='add_post_view'),
    path('detailPost/<post_id>/', views.post_detail_view, name="post_detail_view"),
    path('updatePost/<post_id>/', views.post_update_view, name="post_update_view"),
    path('deletePost/<post_id>/', views.post_delete_view, name="post_delete_view"),
]

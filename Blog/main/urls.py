from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home_view, name="home_view"),
    path("main/add_post.html/", views.add_post_view, name="add_post_view"),
    path("main/Posts.html/", views.Posts_view, name="Posts_view"),
    path("main/post_detail.html/<post_id>/", views.post_detail_view, name="post_detail_view"),
    path("main/update/<post_id>/", views.post_update_view, name="post_update_view"),
    path("delete/<post_id>/", views.post_delete_view, name="post_delete_view"),
    path("search/", views.posts_search_view, name="posts_search_view"),

]

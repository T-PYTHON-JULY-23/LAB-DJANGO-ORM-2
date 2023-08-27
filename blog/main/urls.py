from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("all/", views.add_post_view, name="add_post_view"),
    path("add/", views.all_posts_view, name="all_posts_view"),
    path("detail/<post_id>/", views.post_detail_view, name="post_detail_view"),
    path("update/<post_id>/", views.update_view, name="update_view"),
    path("delete/<post_id>/", views.delete_view, name="delete_view"),
    # path("filter/", views.filter_view, name="filter_view")
]
from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("add/", views.add_post_view, name="add_post_view"),
    path("all/", views.all_post_view, name="all_post_view"),
    path("details/<blog_id>/",views.details_post_view,name="details_post_view"),
    path("update/<blog_id>/", views.update_post_view, name="update_post_view"),
    path("delete/<blog_id>/", views.delete_post_view, name="delete_post_view"),
]

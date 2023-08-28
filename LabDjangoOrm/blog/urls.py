from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.blog_view, name="blog_view"),
    path("all/", views.all_blog_view, name="all_blog_view"),
    path("add/", views.add_new_blog, name="add_new_blog"),
    path("del/<blog_id>/", views.del_blog, name="del_blog"),
    path("detels/<blog_id>/", views.blog_detail, name="blog_detail"),
    path("update/<blog_id>/", views.blog_update, name="blog_update"),
    path("search/", views.search_blog, name="search_blog"),
    # path("search_category/", views.search_category, name="search_category"),
]
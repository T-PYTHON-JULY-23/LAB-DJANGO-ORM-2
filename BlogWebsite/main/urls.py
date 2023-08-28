from django.urls import path
from . import views

app_name ='main'

urlpatterns = [
    path("", views.home_view, name='home_view' ),
    path("write/", views.add_blog_view, name='add_blog_view' ),
    path("detail/<blog_id>/", views.blog_detail_view, name="blog_detail_view"),
    path("update/<blog_id>/", views.blog_update_view, name="blog_update_view"),
    path("delete/<blog_id>/", views.blog_delete_view, name="blog_delete_view"),
    path("search/",views.bolg_search, name="bolg_search"),
]
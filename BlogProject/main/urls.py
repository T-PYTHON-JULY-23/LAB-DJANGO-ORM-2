from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.posts, name='posts'),
    path('add_post/', views.add_post, name='add_post'),
    path("detail/<post_id>/", views.detail_page, name="detail_page"),
    path("update/<post_id>/", views.update_post, name="update_post"),
    path("delete/<posr_id>/", views.delete_post, name="delete_post"),
]

    


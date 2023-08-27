from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('posts/', views.posts, name='posts'),
    path('add_post/', views.add_post, name='add_post'),
     path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/update/', views.update_post, name='update_post'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
    path('search/', views.search_posts, name='search_posts'),
]
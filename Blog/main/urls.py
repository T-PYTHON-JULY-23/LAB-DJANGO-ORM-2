from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home, name="home_view"),
    path('posts/', views.all_recpies, name="post_view"),
    path('add/', views.addRecpie, name="add_recpie"),
    path('notfound/', views.not_found, name="not_fond"),
    path('detali/<recpie_id>/', views.detail_recpie, name="detail_recpie"),
    path('update/<recpie_id>/', views.update_recpie, name="update_recpie"),
    path('delete/<recpie_id>/', views.delete_recpie, name="delete_recpie"),
       

    


    ]
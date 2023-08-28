from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home_page_view, name="home_page_view"),
    path('add/', views.add_new_view, name="add_new_view"),
    path('all/', views.all_new_view, name="all_new_view"),
    path('detalis/<new_id>/', views.detail_view, name="detail_view"),
    path('delet/<new_id>/', views.delete_view, name="delete_view"),
    path('updeat/<new_id>/', views.updeat_view, name="updeat_view"),
    path("search/", views.search_view, name="search_view"),


]
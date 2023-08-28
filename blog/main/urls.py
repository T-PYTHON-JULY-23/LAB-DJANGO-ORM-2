from django.urls import path,include
from . import views

app_name = 'main'

urlpatterns = [
    path('',views.home_view,name='home_view'),
    path('add/',views.add_view,name='add_view'),
    path('all/',views.all_blogs_view,name='all_blogs_view'),
    path('search/',views.search_blogs_view,name='search_blogs_view'),
    path("detail/<post_id>/", views.post_detail_view, name="post_detail_view"),
    path("update/<post_id>/", views.post_update_view, name="post_update_view"),
    path("delete/<post_id>/", views.post_delete_view, name="post_delete_view"),
]
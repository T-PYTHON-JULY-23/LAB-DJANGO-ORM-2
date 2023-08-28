from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('',views.home, name='home_view'),
    path('add_post/',views.add_post,name='add_post_view'),
    path('all_post/',views.view_post,name='all_post_view'),
    path('detail/<post_id>/',views.detail_posts,name="detail_post_view"),
    path('update/<post_id>/',views.update_post,name='update_post_view'),
    path('delet/<post_id>/', views.delet_post,name='delet_post_view'),
    path('search_result/', views.search_feature, name='search_result_view')
]
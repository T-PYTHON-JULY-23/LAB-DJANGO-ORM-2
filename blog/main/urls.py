from django.urls import path,include
from . import views

app_name = 'main'

urlpatterns = [
    path('',views.home_view,name='home_view'),
    path('add/',views.addblog_view,name='addblog_view'),
    path('all/',views.all_bolgs_view,name='all_bolgs_view'),
    path('detail/<blog_id>',views.blog_detail_view,name='blog_detail_view'),
    path('update/<blog_id>',views.blog_update_view,name='blog_update_view'),
    path('delete/<blog_id>',views.blog_delete_view,name='blog_delete_view'),
    path('search/',views.blog_search_view,name='blog_search_view'),

]
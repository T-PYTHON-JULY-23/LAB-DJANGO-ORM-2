from django.urls import path
from . import views
app_name="main"
urlpatterns = [
    path("",views.home_page,name="home_page"),
    path('add/',views.add_page,name="add_page"),
    path("detail/<blog_id>/", views.blog_detail_view, name="blog_detail_view"),
    path("update/<blog_id>/", views.blog_update_view, name="blog_update_view"),
    path("delete/<blog_id>/", views.blog_delete_view, name="blog_delete_view"),
    path('search/' ,views.search,name='search')

]

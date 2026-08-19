from django.urls import path
from . import views

app_name = "blogs"
urlpatterns = [
    path('',views.blog_create,name="list"),
    path('new-blog/',views.create_blog,name="new-blog"),
    ]
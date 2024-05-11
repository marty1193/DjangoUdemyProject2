from django.urls import path
from . import views

# adding path details for the app
urlpatterns = [
    path("",views.starting_page, name="starting_page"),
    path("posts",views.posts, name="posts-page"),
    path("posts/<slug>",views.post_detail, name="post_detail-page")  # posts/my-first-post

]

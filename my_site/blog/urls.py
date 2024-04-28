from django.urls import path
from . import views

# adding path details for the app
urlpatterns = [
    path("",views.starting_page),
    path("posts",views.posts),
    path("posts/<slug>",views.post_detail)  # posts/my-first-post

]

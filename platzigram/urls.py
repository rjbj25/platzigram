from django.urls import path
from platzigram import views as local_views
from posts import views as post_views

urlpatterns = [
    path('hello-world/', local_views.hello_world),
    path('hi/', local_views.hi),
    path('posts', post_views.list_posts)
]

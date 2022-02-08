from django.urls import path

# from . import views
from .views import (
    HomeView,
    ArticleDetailView,
    CreatePostView,
    UpdatePostView,
    DeletePostView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("article/<int:pk>", ArticleDetailView.as_view(), name="article-detail"),
    path("create", CreatePostView.as_view(), name="create-post"),
    path("article/edit/<int:pk>", UpdatePostView.as_view(), name="update-post"),
    path("article/<int:pk>/delete", DeletePostView.as_view(), name="post_delete"),
]

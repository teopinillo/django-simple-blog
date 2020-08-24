from django.urls import path

from .views import BlogListView, login_view, logout_view, register, BlogDetailView
from .views import BlogCreateView
from .views import BlogUpdateView
from .views import BlogDeleteView

urlpatterns = [
    path ('post/<int:pk>/delete/',BlogDeleteView.as_view(), name='post_delete'),
    path ('post/<int:pk>/edit/',BlogUpdateView.as_view(), name='post_edit'),
    path ('post/new/', BlogCreateView.as_view(), name='post_new'),
    path ('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path ('', BlogListView.as_view(), name='home'),
    path("login", login_view, name="login"),
    path("logout", logout_view, name="logout"),
    path("register", register, name="register"),
]
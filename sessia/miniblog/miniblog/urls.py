"""
URL configuration for miniblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostListCreateView.as_view()),
    path('posts/<int:pk>/', views.PostRetrieveUpdateDestroyView.as_view()),
    path('posts/<int:post_id>/comments/', views.CommentListCreateView.as_view()),
    path('posts/<int:post_id>/comments/<int:pk>/', views.CommentRetrieveUpdateDestroyView.as_view()),
]


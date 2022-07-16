from django.urls import path 
from .views import PostCreateView, PostDetailView, PostListView 


urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('new/', PostCreateView.as_view(), name='post_new'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]
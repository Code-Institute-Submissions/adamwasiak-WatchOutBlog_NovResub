from . import views
from .views import DeleteComment
from django.urls import path

# Paths for all required views
urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('delete_comment/<int:pk>', views.DeleteComment.as_view(),
         name='delete_comment'),
    path('update_comment/<int:pk>', views.UpdateComment.as_view(),
         name='update_comment')
]

from django.urls import path
from content import views as content_views

urlpatterns = [
    path('content', content_views.content_view, name='content'),
]

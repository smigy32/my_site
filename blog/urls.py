from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r"posts", views.PostViewSet)

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("posts/", views.PostsView.as_view(), name="posts-page"),
    path("posts/<slug:slug>/", views.PostDetailView.as_view(),
         name="post-detail-page"),  # /posts/my-first-post
    path("read-later/", views.ReadLaterView.as_view(), name="read-later"),
    path("api/v1/", include(router.urls)),  # http://127.0.0.1:8000/api/v1/posts/ and http://127.0.0.1:8000/api/v1/posts/<int:pk>
    
    # path("api/v1/posts/", views.PostViewSet.as_view({"get": "list"})),
    # path("api/v1/posts/<int:pk>/", views.PostViewSet.as_view({"put": "update"})),
]

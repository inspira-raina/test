# myapi/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r"^books", BookViewSet)

urlpatterns = [
    # path(r"^", include(router.urls)),
]

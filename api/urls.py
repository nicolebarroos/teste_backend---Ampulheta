from rest_framework import routers
from django.urls import path, include

from api.views import UsersViewSet

router = routers.DefaultRouter()
router.register(r'users', UsersViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls))
]
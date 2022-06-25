from rest_framework import routers
from django.urls import path, include

from api.views import UsersViewSet, TimeViewSet, ProjectViewSet

router = routers.DefaultRouter()
router.register(r'users', UsersViewSet, basename='users')
router.register(r'times', TimeViewSet, basename='times')
router.register(r'project', ProjectViewSet, basename='projects')

urlpatterns = [
    path('', include(router.urls))
]
from django.conf.urls import url, include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('person', PersonViewSet)
router.register('use_login', PersonViewSet)

urlpatterns = [
    url(r'user_login$', user_login),
    url('', include(router.urls))
]
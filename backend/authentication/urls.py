
from django.conf.urls import include, url
from django.urls import reverse
from .views import (
    LoginAPIView, RegistrationAPIView, UserRetrieveUpdateAPIView, UserViewSet
)
from rest_framework.routers import DefaultRouter


app_name = 'authentication'

router = DefaultRouter()

#Admin
router.register(r'^userlist', UserViewSet)
router.register(r'^userdetail', UserViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),


    url(r'^user/?$', UserRetrieveUpdateAPIView.as_view()),
    url(r'^users/?$', RegistrationAPIView.as_view()),
    url(r'^users/login/?$', LoginAPIView.as_view()),

    #Admin                               
    # url(r'^userdetail/(?P<username>[0-9a-zA-Z_-]+)/$', UserViewSet.as_view( {'get': 'retrieve'} ))
]

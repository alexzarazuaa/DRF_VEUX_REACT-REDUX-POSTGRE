from django.conf.urls import include, url
from django.urls import reverse
from .views import ProfileRetrieveAPIView, ProfileViewSet
from rest_framework.routers import DefaultRouter

app_name = 'profiles'

router = DefaultRouter()

#Admin
router.register(r'^profilelist', ProfileViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),

    url(r'^profiles/(?P<username>\w+)/?$', ProfileRetrieveAPIView.as_view()),
]

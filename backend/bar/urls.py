from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

from .views import SongViewSet

app_name = 'bar'

# router = DefaultRouter(trailing_slash=False)
# router.register(r'bar', SongViewSet, basename='bar')

# urlpatterns = [
#     url(r'^', include(router.urls)),

# ]
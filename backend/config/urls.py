from django.conf.urls import include, url
from django.contrib import admin
from django.urls import reverse

urlpatterns = [
    url('admin/', admin.site.urls),
    url('api-auth/', include('rest_framework.urls')),

    url('api/', include('bars.urls')),
    url('api/', include('authentication.urls')),
    url('api/', include('profiles.urls')),
]


from rest_framework import generics, mixins, status, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.permissions import (
    AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
)
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Bar
from .renderers import BarJSONRenderer
from .serializers import BarSerializer

#Admin
class BarViewSetAdmin(viewsets.ModelViewSet):
    queryset = Bar.objects.all()
    serializer_class = BarSerializer
    lookup_field = 'slug'
    permission_classes = (IsAuthenticated,)
    permission_classes = (IsAdminUser,)
    

class BarViewSet(viewsets.ModelViewSet):
    queryset = Bar.objects.all()
    serializer_class = BarSerializer
    lookup_field = 'slug'


    def get_queryset(self):
        queryset = self.queryset

        owner = self.request.query_params.get('owner', None)
        if owner is not None:
            queryset = queryset.filter(owner__user__username=owner)

        return queryset

    def create(self, request):
        serializer_context = {
            'owner': request.user.profile,
            'request': request
        }
        serializer_data = request.data.get('bar', {})

        serializer = self.serializer_class(
        data=serializer_data, context=serializer_context
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)




# requests.del(`/bar/${slug}`),
class BarsDestroyAPIView(generics.DestroyAPIView):
    lookup_url_kwarg = 'slug'
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Bar.objects.all()

    def destroy(self, request, slug=None):
        try:
            bar = Bar.objects.get(slug=slug)
        except Bar.DoesNotExist:
            raise NotFound('A bar with this slug does not exist.')
        bar.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


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
    
class BarViewSet(mixins.CreateModelMixin, 
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):

    lookup_field = 'slug'
    queryset = Bar.objects.select_related('owner', 'owner__user')
    permission_classes = (IsAuthenticatedOrReadOnly,)
    renderer_classes = (BarJSONRenderer,)
    serializer_class = BarSerializer

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

    def list(self, request):
        serializer_context = {'request': request}
        page = self.paginate_queryset(self.get_queryset())

        serializer = self.serializer_class(
            page,
            context=serializer_context,
            many=True
        )

        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, slug):
        serializer_context = {'request': request}
        try:
            serializer_instance = self.queryset.get(slug=slug)
        except Bar.DoesNotExist:
            raise NotFound('An bar with this slug does not exist.')

        serializer = self.serializer_class(
            serializer_instance,
            context=serializer_context
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


    def update(self, request, slug):
        serializer_context = {'request': request}

        try:
            serializer_instance = self.queryset.get(slug=slug)
        except Bar.DoesNotExist:
            raise NotFound('An bar with this slug does not exist.')
            
        serializer_data = request.data.get('bar', {})

        serializer = self.serializer_class(
            serializer_instance, 
            context=serializer_context,
            data=serializer_data, 
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


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


class BarsFeedAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Bar.objects.all()
    renderer_classes = (BarJSONRenderer,)
    serializer_class = BarSerializer

    def get_queryset(self):
        return Bar.objects.filter(
            owner__in=self.request.user.profile.follows.all()
        )

    def list(self, request):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)

        serializer_context = {'request': request}
        serializer = self.serializer_class(
            page, context=serializer_context, many=True
        )

        return self.get_paginated_response(serializer.data)

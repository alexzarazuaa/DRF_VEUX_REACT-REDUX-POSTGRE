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

class BarsFavoriteAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (BarJSONRenderer,)
    serializer_class = BarSerializer

    def delete(self, request, bar_slug=None):
        profile = self.request.user.profile
        serializer_context = {'request': request}

        try:
            bar = Bar.objects.get(slug=bar_slug)
        except Bar.DoesNotExist:
            raise NotFound('An bar with this slug was not found.')

        profile.unfavorite(bar)

        serializer = self.serializer_class(bar, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, bar_slug=None):
        profile = self.request.user.profile
        serializer_context = {'request': request}

        try:
            bar = Bar.objects.get(slug=bar_slug)
        except Bar.DoesNotExist:
            raise NotFound('An bar with this slug was not found.')

        profile.favorite(bar)

        serializer = self.serializer_class(bar, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class BarsBookViewSet(mixins.CreateModelMixin, 
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
                     
    # lookup_field = 'slug'
    queryset = Bar.objects.select_related('author', 'author__user')
    renderer_classes = (BarJSONRenderer,)
    serializer_class = BarSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, bar_slug):
        try:
            bar = Bar.objects.get(slug=bar_slug)
        except Bar.DoesNotExist:
            raise NotFound('An bar with this slug was not found.')

        profile = self.request.user.profile
        time = request.data.get('time')
        profile.book(bar, time)

        serializer = self.serializer_class(bar, context={'request': request})

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, bar_slug , *args, **kwargs):

        try:
            bar = Bar.objects.get(slug=bar_slug)
        except Bar.DoesNotExist:
            raise NotFound('An bar with this slug was not found.')

        serializer = self.serializer_class(bar, context={'request': request})
 

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, bar_slug=None):

        try:
            bar = Bar.objects.get(slug=bar_slug)
        except Bar.DoesNotExist:
            raise NotFound('An bar with this slug was not found.')

        profile = self.request.user.profile
        profile.unbook(bar)
        
        serializer = self.serializer_class(bar, context={'request': request})

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, slug):

        try:
            serializer_instance = self.queryset.get(slug=slug)
        except Article.DoesNotExist:
            raise NotFound('An article with this slug does not exist.')
            
        serializer_data = request.data.get('time')




        serializer = self.serializer_class(bar, context={'request': request})

        return Response(serializer.data, status=status.HTTP_200_OK)
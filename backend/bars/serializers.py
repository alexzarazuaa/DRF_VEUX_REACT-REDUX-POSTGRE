from rest_framework import serializers

from profiles.serializers import ProfileSerializer

from .models import Bar

class BarSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer(read_only=True)
    description = serializers.CharField(required=False)
    slug = serializers.SlugField(required=False)

    favorited = serializers.SerializerMethodField()
    favoritesCount = serializers.SerializerMethodField(
        method_name='get_favorites_count'
    )

    bookingsCount = serializers.SerializerMethodField(
        method_name='get_bookings_count'
    )

    # Django REST Framework makes it possible to create a read-only field that
    # gets it's value by calling a function. In this case, the client expects
    # `created_at` to be called `createdAt` and `updated_at` to be `updatedAt`.
    # `serializers.SerializerMethodField` is a good way to avoid having the
    # requirements of the client leak into our API.
    createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = Bar
        fields = (
            'slug',
            'name',
            'description',
            'owner',
            'favorited',
            'favoritesCount',
            'bookingsCount',
            'createdAt',
            'updatedAt',
        )

    def create(self, validated_data):
        owner = self.context.get('owner', None)

        bar = Bar.objects.create(owner=owner, **validated_data)

        return bar

    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()

    def get_favorited(self, instance):
        request = self.context.get('request', None)

        if request is None:
            return False

        # if not request.user.is_authenticated():
        if not request.user.is_authenticated:
            return False

        return request.user.profile.has_favorited(instance)

    def get_favorites_count(self, instance):
        return instance.favorited_by.count()

    def get_bookings_count(self, instance):
        return instance.booking_by.count()
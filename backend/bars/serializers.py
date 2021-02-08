from rest_framework import serializers

from profiles.serializers import ProfileSerializer

from .models import Bar

class BarSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer(read_only=True)
    description = serializers.CharField(required=False)
    slug = serializers.SlugField(required=False)



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
            'owner',
            'body',
            'createdAt',
            'description',
            'slug',
            'title',
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

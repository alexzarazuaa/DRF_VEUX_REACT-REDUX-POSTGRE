from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    bio = serializers.CharField(allow_blank=True, required=False)
    image = serializers.CharField(allow_blank=True, required=False)
<<<<<<< HEAD
    favorited = serializers.SerializerMethodField()

    # image = serializers.SerializerMethodField()
=======
>>>>>>> e43a151cec4c4daebbe5b949990658ff3ad0623d
    class Meta:
        model = Profile
        fields = ('username', 'bio', 'image', 'favorited',)
        read_only_fields = ('username',)


    def get_favorited(self, instance):
        request = self.context.get('request', None)

        if request is None:
            return False

        # if not request.user.is_authenticated():
        if not request.user.is_authenticated:
            return False

        return request.user.profile.has_favorited(instance)
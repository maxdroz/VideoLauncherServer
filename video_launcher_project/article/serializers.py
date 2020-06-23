from rest_framework import serializers

from article.views import User

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    token = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.token = validated_data.get('token', instance.token)
        instance.save()
        return instance
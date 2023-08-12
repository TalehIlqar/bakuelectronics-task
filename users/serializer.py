from rest_framework import serializers

from .models import MyUser as User, BlockedIP


class GetUserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("full_name", "id")

    def get_full_name(self, obj):
        return obj.first_name + " " + obj.last_name


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password", "first_name", "last_name", "email")


class BlockedIPSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockedIP
        fields = ("ip",)

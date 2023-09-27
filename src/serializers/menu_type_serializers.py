from rest_framework import serializers

from src.models import MenuType


class MenuTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuType
        fields = "__all__"

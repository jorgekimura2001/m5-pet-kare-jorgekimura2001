from rest_framework import serializers
# from .models import Trait
# from rest_framework.validators import UniqueValidator
# from rest_framework.views import status


class TraitSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=10)
    created_at = serializers.DateTimeField(read_only=True)

    # def create(self, validated_data):
    #     trait, exists = Trait.objects.get_or_create(**validated_data)

    #     if not exists:
    #         raise ValueError(
    #             {"message": "Group already exists"},
    #             status.HTTP_409_CONFLICT,
    #         )

    #     return trait

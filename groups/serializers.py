from rest_framework import serializers
# from rest_framework.validators import UniqueValidator
# from .models import Group
# from rest_framework.views import status


class GroupSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    scientific_name = serializers.CharField(
        max_length=50,
    )
    created_at = serializers.DateTimeField(read_only=True)

    # def create(self, validated_data):
    #     group, exists = Group.objects.get_or_create(**validated_data)

    #     if not exists:
    #         raise ValueError(
    #             {"message": "Group already exists"},
    #             status.HTTP_409_CONFLICT,
    #         )

    #     return group

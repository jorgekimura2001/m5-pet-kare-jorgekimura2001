from rest_framework import serializers
from traits.serializers import TraitSerializer
from groups.serializers import GroupSerializer
from .models import Pet, PetSex


class PetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(
        choices=PetSex.choices,
        default=PetSex.NOT_INFORMED,
    )
    group = GroupSerializer()
    traits = TraitSerializer(many=True)

    def create(self, validated_data):
        return Pet.objects.create(**validated_data)

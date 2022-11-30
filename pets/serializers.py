from rest_framework import serializers
from traits.serializers import TraitSerializer
from groups.serializers import GroupSerializer
from .models import Pet, PetSex
from groups.models import Group
from traits.models import Trait
import ipdb


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
        request_group = validated_data.pop('group')
        group, _ = Group.objects.get_or_create(**request_group)
        validated_data["group"] = group
        traits = validated_data.pop("traits")
        pet = Pet.objects.create(**validated_data)
        for trait in traits:
            trait_request, _ = Trait.objects.get_or_create(**trait)
            pet.traits.add(trait_request)

        return pet

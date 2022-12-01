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
    traits_count = serializers.SerializerMethodField()

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

    def update(self, instance, validated_data):
        trait_updated = []
        for key, value in validated_data.items():
            if key == 'group':
                group, _ = Group.objects.get_or_create(**value)
                instance.group = group
            elif key == 'traits':
                for trait in value:
                    trait_request, _ = Trait.objects.get_or_create(**trait)
                    trait_updated.append(trait_request)
                instance.traits.set(trait_updated)
            else:
                setattr(instance, key, value)

        instance.save()
        return instance

    def get_traits_count(self, obj):
        return len(obj.traits.all())

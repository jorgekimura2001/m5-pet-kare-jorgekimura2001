from rest_framework.views import APIView, Request, Response, status
from .models import Pet
from .serializers import PetSerializer
import ipdb
from django.shortcuts import get_object_or_404


class PetView(APIView):
    def get(self, request: Request) -> Response:
        pets = Pet.objects.all()

        serializer = PetSerializer(pets, many=True)

        # ipdb.set_trace()
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = PetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class PetViewParams(APIView):
    def get(self, request: Request, pet_id) -> Response:
        pet = get_object_or_404(Pet, id=pet_id)
        serializer = PetSerializer(pet)

        return Response(serializer.data)

    def patch(self, request: Request, pet_id) -> Response:
        pet = get_object_or_404(Pet, id=pet_id)
        serializer = PetSerializer(pet, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request: Request, pet_id) -> Response:
        pet = get_object_or_404(Pet, id=pet_id)
        pet.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

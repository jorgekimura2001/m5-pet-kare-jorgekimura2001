from rest_framework.views import APIView, Request, Response, status
from .models import Pet
from .serializers import PetSerializer
import ipdb


class PetView(APIView):
    def get(self, request: Request) -> Response:
        pets = Pet.objects.all()

        serializer = PetSerializer(pets, many=True)

        # ipdb.set_trace()
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = PetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ipdb.set_trace()
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class PetViewParams(APIView):
    def get(self, request: Request, pet_id) -> Response:
        ...

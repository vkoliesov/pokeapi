from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.serializers import PokemonSerializer

from services.get_pokemons_service import get_pokemons


@csrf_exempt
def pokemon_list(request):
    serializer = PokemonSerializer(get_pokemons(), many=True)

    if request.method == 'GET':
        return JsonResponse(serializer.data, safe=False)
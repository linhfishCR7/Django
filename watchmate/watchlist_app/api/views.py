from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MoiveSerializer

@api_view()
def movie_list(request):
    movies = Movie.objects.all()
    # when we have multiple objects, we need to find many equals(need to visit each element and then map it)
    # Serializer need to visit multiple objects. Only single query 
    serializers = MoiveSerializer(movies, many=True) 
    return Response(serializers.data)

@api_view()
def movie_details(request,pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MoiveSerializer(movie)
    return Response(serializer.data)
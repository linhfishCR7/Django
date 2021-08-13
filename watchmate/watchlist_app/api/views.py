from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MoiveSerializer
@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        # when we have multiple objects, we need to find many equals(need to visit each element and then map it)
        # Serializer need to visit multiple objects. Only single query 
        serializers = MoiveSerializer(movies, many=True) 
        return Response(serializers.data)
    if request.method =='POST':
        serializer = MoiveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, )
        else:
            return Response(serializer.errors)
@api_view(['GET', 'PUT', 'DELETE'])
def movie_details(request,pk):
        if request.method == 'GET':
            # try catch exception to test id exist or not
            try:
                movie = Movie.objects.get(pk=pk)
            except Movie.DoesNotExist:
                return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = MoiveSerializer(movie)
            return Response(serializer.data)
        if request.method == 'PUT':
            movie = Movie.objects.get(pk=pk)
            serializer = MoiveSerializer(movie,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'DELETE':
             movie = Movie.objects.get(pk=pk)
             movie.delete()
             return Response(status=status.HTTP_204_NO_CONTENT) # status code when it was deleted


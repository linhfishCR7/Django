from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from cities_app.models import City
from cities_app.api.serializers import CitySerializer

@api_view(['GET', 'POST'])
def city_list(request):
    if request.method == 'GET':
        cities = City.objects.all()
        # when we have multiple objects, we need to find many equals(need to visit each element and then map it)
        # Serializer need to visit multiple objects. Only single query 
        serializers = CitySerializer(cities, many=True) 
        return Response(serializers.data)
    if request.method =='POST':
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, )
        else:
            return Response(serializer.errors)
@api_view(['GET', 'PUT', 'DELETE'])
def city_details(request,pk):
        if request.method == 'GET':
            # try catch exception to test id exist or not
            try:
                cities = City.objects.get(pk=pk)
            except City.DoesNotExist:
                return Response({'error': 'City not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = CitySerializer(cities)
            return Response(serializer.data)
        if request.method == 'PUT':
            city = City.objects.get(pk=pk)
            serializer = CitySerializer(city,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'DELETE':
             city = City.objects.get(pk=pk)
             city.delete()
             return Response(status=status.HTTP_204_NO_CONTENT) # status code when it was deleted


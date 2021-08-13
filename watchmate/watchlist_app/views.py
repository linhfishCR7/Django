# from django.shortcuts import render
# from watchlist_app.models import Movie # from model
# from django.http import JsonResponse
# # Create your views here.

# def movie_list(request): #get all data
#     movies = Movie.objects.all()
#     # print(movies.values())
#     data = {
#         "movies":list( movies.values())
#     }
#     return JsonResponse(data)


# def movie_details(request,pk): # get one data by pk(id)
#     movie = Movie.objects.get(pk=pk)
#     data = {
#         "name": movie.name,
#         "description": movie.description,
#         "active": movie.active
#     }
#     return JsonResponse(data)
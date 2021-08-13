from django.urls import path, include
from watchlist_app.api.views import movie_details, movie_list # add form function in view
urlpatterns = [
    path('list/', movie_list , name='movie-list'),
    path('<int:pk>', movie_details , name='movie-details'),
]
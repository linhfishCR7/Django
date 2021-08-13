from django.urls import path, include
from cities_app.api.views import city_details, city_list # add form function in view
urlpatterns = [
    path('list/', city_list , name='city-list'),
    path('<int:pk>', city_details , name='city-details'),
]
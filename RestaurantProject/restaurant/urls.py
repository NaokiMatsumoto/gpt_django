from django.urls import path
from .views import PrefectureCitiesView, CityRestaurantsView, RestaurantDetailView, RestaurantListView


# The API URLs are determined automatically by the router
urlpatterns = [
    # path('prefectures/<int:prefecture_id>/cities/', PrefectureCitiesView.as_view(), name='prefecture-cities-web'),
    # path('cities/<int:city_id>/restaurants/', CityRestaurantsView.as_view(), name='city-restaurants-web'),
    path('restaurants/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant-detail-web'),
    path('restaurants/', RestaurantListView.as_view(), name='restaurant-list-web'),
]

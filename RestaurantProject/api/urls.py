
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PrefectureViewSet, CityViewSet, RestaurantViewSet

# Create a router and register our viewsets
router = DefaultRouter()
router.register(r'prefectures', PrefectureViewSet)
router.register(r'cities', CityViewSet)
router.register(r'restaurants', RestaurantViewSet)

# The API URLs are determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]

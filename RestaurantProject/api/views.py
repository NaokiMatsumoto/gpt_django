from rest_framework import viewsets, filters
from .models import Prefecture, City, Restaurant
from .serializers import PrefectureSerializer, CitySerializer, RestaurantSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination


class SmallPagination(PageNumberPagination):
    page_size = 5  # 一ページあたりのアイテム数


# ReadOnlyModelViewSet for Prefecture
class PrefectureViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Prefecture.objects.all()
    serializer_class = PrefectureSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']  # name フィールドに対する検索を可能にする
    pagination_class = SmallPagination

# ReadOnlyModelViewSet for City
class CityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']  # name フィールドに対する検索を可能にする
    pagination_class = SmallPagination

class RestaurantViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['city_id', 'city__prefecture_id']  # city__prefecture_id で都道府県にフィルタリング
    search_fields = ['name', 'description']
    pagination_class = SmallPagination

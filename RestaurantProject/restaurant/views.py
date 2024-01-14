from django.views import generic
from api.models import Prefecture, City, Restaurant



class RestaurantDetailView(generic.DetailView):
    model = Restaurant
    template_name = 'restaurant_detail.html'


class PrefectureCitiesView(generic.ListView):
    template_name = 'prefecture_cities.html'
    context_object_name = 'cities'
    paginate_by = 10  # 一ページに表示する都道府県の数

    def get_queryset(self):
        return City.objects.filter(prefecture_id=self.kwargs['prefecture_id'])

class CityRestaurantsView(generic.ListView):
    template_name = 'city_restaurants.html'
    context_object_name = 'restaurants'
    paginate_by = 10  # 一ページに表示する市の数


class RestaurantListView(generic.ListView):
    model = Restaurant
    template_name = 'restaurant_list.html'
    context_object_name = 'restaurants'
    paginate_by = 10  # 一ページに表示するレストランの数

from rest_framework import serializers
from django.urls import reverse
from .models import Restaurant, Prefecture, City

# Serializer for Prefecture
class PrefectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prefecture
        fields = '__all__'

# Serializer for City
class CitySerializer(serializers.ModelSerializer):
    prefecture = PrefectureSerializer(read_only=True)

    class Meta:
        model = City
        fields = '__all__'

# Serializer for Restaurant
class RestaurantSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    detail_url = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = ('name', 'description', 'address', 'phone_number', 'city',  'detail_url',)

    def get_detail_url(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(reverse('restaurant-detail-web', args=[obj.pk]))
        return None

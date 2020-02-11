from rest_framework import serializers

from news.models import *

class ProductsSalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products_Sales
        fields = ('__all__')

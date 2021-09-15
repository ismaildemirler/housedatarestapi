from rest_framework import serializers
from .models import AverageHousePrice, NumberOfTransactions


class AverageHousePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AverageHousePrice
        fields = [
            'average_price',
            'year_month',
            'home_type',
        ]


class NumberOfTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumberOfTransactions
        fields = [
        ]

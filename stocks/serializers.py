from rest_framework import serializers
from .models import Watchlist, Stock

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id', 'symbol']

class WatchlistSerializer(serializers.ModelSerializer):
    stocks = StockSerializer(many=True)

    class Meta:
        model = Watchlist
        fields = ['id', 'name', 'stocks']
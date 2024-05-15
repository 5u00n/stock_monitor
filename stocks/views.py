from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Watchlist, Stock
from .serializers import WatchlistSerializer, StockSerializer
from django.conf import settings
import requests

class WatchlistView(APIView):
    def get(self, request):
        watchlists = Watchlist.objects.filter(user=request.user)
        serializer = WatchlistSerializer(watchlists, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StockDataView(APIView):
    def get(self, request, symbol):
        api_key = settings.ALPHAVANTAGE_API_KEY
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={api_key}'
        response = requests.get(url)
        data = response.json()
        return Response(data)


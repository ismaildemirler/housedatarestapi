from django.db.models.aggregates import Avg, Count, Max, Min
from django.db.models.functions.text import Concat
from rest_framework.response import Response
from api.models import HousesData
from rest_framework import viewsets
from . import serializers
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models.functions import ExtractMonth, ExtractYear


class AverageHousePricesViewset(viewsets.ModelViewSet):
    serializer_class = serializers.AverageHousePriceSerializer
    filter_backends = (OrderingFilter, SearchFilter, DjangoFilterBackend)

    search_fields = ['house_id', 'price', 'post_code',
                     'transaction_date', 'home_type', 'end_date', 'beginning_date']

    def get_queryset(self):
        post_code = self.request.query_params.get('post_code', None)
        end_date = self.request.query_params.get('end_date', None)
        beginning_date = self.request.query_params.get('beginning_date', None)

        queryset = HousesData.objects.all()

        if post_code:
            queryset = HousesData.objects.get_house_by_location(post_code)

        if beginning_date and end_date:
            beginning_date = beginning_date + "-01"
            end_date = end_date + "-30"
            date_range_queryset = HousesData.objects.get_house_between_end_beginning_date(
                beginning_date, end_date)

            queryset = queryset & date_range_queryset

            queryset = queryset.annotate(year=ExtractYear('transaction_date'), month=ExtractMonth('transaction_date')).annotate(
                year_month=Concat(ExtractYear('transaction_date'), ExtractMonth('transaction_date'))).annotate(
                average_price=Avg('price')).values('average_price', 'home_type', 'year_month').annotate(
                count=Count('year_month')).order_by('year', 'month')

        return queryset


class NumberOfTransactionViewset(viewsets.ModelViewSet):

    queryset = HousesData.objects.all()
    serializer_class = serializers.NumberOfTransactionSerializer
    filter_backends = (OrderingFilter, SearchFilter, DjangoFilterBackend)

    search_fields = ['house_id', 'price', 'post_code',
                     'transaction_date', 'home_type', 'end_date', 'beginning_date']

    def list(self, request, *args, **kwargs):
        transactions = []
        post_code = self.request.query_params.get('post_code', None)
        transaction_date = self.request.query_params.get(
            'transaction_date', None)

        queryset = HousesData.objects.all()
        if post_code:
            queryset = HousesData.objects.get_house_by_location(post_code)

        if transaction_date:
            beginning_date = transaction_date + "-01"
            end_date = transaction_date + "-30"
            date_range_queryset = HousesData.objects.get_house_between_end_beginning_date(
                beginning_date, end_date)

            queryset = queryset & date_range_queryset

            if not queryset:
                transaction = {"message": "There is no item"}
                transactions.append(transaction)
            else:
                reduced_queryset = queryset.annotate(
                    year_month=Concat(ExtractYear('transaction_date'), ExtractMonth('transaction_date'))).annotate(
                    min_price=Min('price'), max_price=Max('price')).values(
                    'min_price', 'max_price', 'year_month').annotate(
                    count=Count('year_month'))

                min_price = reduced_queryset[0]['min_price']
                max_price = reduced_queryset[0]['max_price']
                count = reduced_queryset[0]['count']

                step = round((max_price - min_price)/count) + 1

                queryset = queryset.values('price')
                less_number = min_price
                less_number_str = str(less_number)[:-3]
                for i in range(8):
                    point = min_price + step*(i+1)
                    point_str = str(point)[:-3]

                    item_count = queryset.filter(
                        price__gte=less_number, price__lte=point).count()

                    if(i == 0):
                        transaction = {"price_range": "Under €" +
                                    point_str+"k", "transaction_count": item_count}
                    elif(i == 7):
                        transaction = {"price_range": "Over €" +
                                    less_number_str+"k", "transaction_count": item_count}
                    else:
                        transaction = {"price_range":
                                    "€"+less_number_str+"k - €"+point_str+"k",
                                    "transaction_count": item_count}
                    less_number = point
                    less_number_str = str(less_number)[:-3]
                    transactions.append(transaction)
            
        return Response(transactions)

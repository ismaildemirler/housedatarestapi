from django.db.models.aggregates import Count, Max, Min
from django.db.models.functions.datetime import ExtractMonth, ExtractYear
from django.db.models.functions.text import Concat
from django.http.response import HttpResponse
from .models import HousesData

# The other way
def transaction_view(request):
    post_code = request.GET.get('post_code', None)
    transaction_date = request.GET.get(
        'transaction_date', None)

    queryset = HousesData.objects.all()
    transactions = []

    if post_code:
        queryset = HousesData.objects.get_house_by_location(post_code)

    if transaction_date:
        beginning_date = transaction_date + "-01"
        end_date = transaction_date + "-30"
        date_range_queryset = HousesData.objects.get_house_between_end_beginning_date(
            beginning_date, end_date)

        queryset = queryset & date_range_queryset

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
        print(queryset)
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
    
    return HttpResponse(transactions)

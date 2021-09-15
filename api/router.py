from api.viewsets import AverageHousePricesViewset, NumberOfTransactionViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('averagehouseprices', AverageHousePricesViewset, basename='averagehouseprices')
router.register('numberoftransactions', NumberOfTransactionViewset, basename='numberoftransactions')
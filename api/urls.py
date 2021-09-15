from api.views import transaction_view
from django.urls import path, include
from .router import router
# from .views import HouseList

urlpatterns = [
    path('', include(router.urls)),
    # path('numberoftransactions/', transaction_view)
]

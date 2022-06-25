from django.urls import path
from .views import LapakList

urlpatterns = [
    path('', LapakList.as_view(), name="lapak-list"),
]

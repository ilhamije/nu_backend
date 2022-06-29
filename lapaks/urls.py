from django.urls import path
from .views import LapakList

app_name = "lapaks"

urlpatterns = [
    path('', LapakList.as_view(), name="lapak-listing"),
]

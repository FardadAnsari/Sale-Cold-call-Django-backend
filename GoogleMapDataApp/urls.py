from django.urls import path
from . import views

app_name = 'GoogleMapDataApp'

urlpatterns = [
    path('', views.GoogleMapShopDataAPIView.as_view(), name='google-map-data'),

]
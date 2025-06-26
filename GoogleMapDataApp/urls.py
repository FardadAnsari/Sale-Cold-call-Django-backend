from django.urls import path
from . import views

app_name = 'GoogleMapDataApp'

urlpatterns = [
    path('', views.GoogleMapDataAPIView.as_view(), name='google-map-report-table'),

]
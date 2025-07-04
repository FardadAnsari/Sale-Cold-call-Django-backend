from django.urls import path
from . import views

app_name = 'HistoryApp'

urlpatterns = [
    path('', views.HistoryAPIView.as_view(), name='HistoryApp'),
    path('<int:pk>', views.HistoryDetailAPIView.as_view(), name='HistoryApp'),
]
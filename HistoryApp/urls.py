from django.urls import path
from . import views

app_name = 'HistoryApp'

urlpatterns = [
    path('', views.HistoryAPIView.as_view(), name='HistoryApp'),
    path('<int:pk>', views.HistoryDetailAPIView.as_view(), name='HistoryApp'),
    path('call-history/', views.CustomerListAPIView.as_view(), name='customer-list'),
    path('shop-detail/<int:pk>/', views.CustomerDetailAPIView.as_view(), name='customer-detail'),
    path('call-form-submit/', views.CustomerCallFormSubmitView.as_view(), name='customer-form'),



    path('stages/', views.StageListAPIView.as_view(), name='stage-list'),
    # path('stages/<int:pk>/', views.StageDetailAPIView.as_view(), name='stage-detail'),
    path('case-sessions/', views.SaleSessionListAPIView.as_view(), name='salesession-list'),
    path('case-sessions/create/', views.SaleSessionCreateAPIView.as_view(), name='salesession-create'),
    path('case-sessions-update/<int:pk>/', views.SaleSessionUpdateAPIView.as_view(), name='salesession-update'),
    path('case-sessions-detail/<int:pk>/', views.SaleSessionDetailAPIView.as_view(), name='salesession-detail'),

]
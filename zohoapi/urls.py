from django.urls import path
from .views import CreateZohoLeadView

urlpatterns = [
    path('call-to-customer/', CreateZohoLeadView.as_view(), name='create-zoho-lead'),
]

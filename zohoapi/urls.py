from django.urls import path
from .views import CreateZohoLeadView

urlpatterns = [
    path('create-lead', CreateZohoLeadView.as_view(), name='create-zoho-lead'),
]

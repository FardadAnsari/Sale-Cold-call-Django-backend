from django.db import models
from accounts_user.models import SaleUser
from GoogleMapDataApp.models import GoogleMapShopsModel


class CustomerModel(models.Model):
    customer_google_business = models.ForeignKey(
        GoogleMapShopsModel,
        to_field='shop_id_company',  
        db_column='customer_google_business',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='customers'
    )
    customer_name = models.CharField(max_length=255, null=True, blank=True)
    customer_phone = models.CharField(max_length=255, null=True, blank=True)
    customer_assistant_phone = models.CharField(max_length=255, null=True, blank=True)
    customer_assistant_name = models.CharField(max_length=255, null=True, blank=True)
    customer_availability = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.customer_name or f"Customer {self.id}"

    class Meta:
        db_table = 'customer'


class StageModel(models.Model):
    name = models.ForeignKey('SaleSessionModel', db_column='name', on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'stage'



 
class SaleSessionModel(models.Model):
    start_time = models.DateTimeField(null=True)
    last_update = models.DateTimeField(null=True)
    close_time = models.DateTimeField(null=True)
    customer = models.ForeignKey(
        'CustomerModel',
        on_delete=models.CASCADE,
        related_name='sale_sessions',
        db_column='customer_id'
    )
    stage = models.CharField(max_length=255, null=True, blank=True, db_column='stage_name')
    created_by = models.ForeignKey(
        SaleUser,
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_sale_sessions',
        db_column='created_by'
    )

    class Meta:
        db_table = 'sale_sessions'

    def str(self):
        return f"Session for {self.customer} on {self.start_time}"

class HistoryModel(models.Model):
    date = models.DateTimeField()

    sale_session = models.ForeignKey(  
        SaleSessionModel,
        on_delete=models.CASCADE,
        db_column='sale_session_id',
        related_name='histories'
    )

    user = models.ForeignKey(  
        SaleUser,
        on_delete=models.CASCADE,
        db_column='user_id',
        related_name='history_entries'
    )

    call_time = models.CharField(max_length=128)
    description = models.TextField()

    class Meta:
        db_table = 'history'

    def __str__(self):
        return f"{self.date} - {self.call_time}"

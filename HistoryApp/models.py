from django.db import models
from accounts_user.models import SaleUser

class HistoryModel(models.Model):
    date = models.DateTimeField()
    sale_session_id = models.IntegerField()
    user_id = models.ForeignKey(SaleUser, on_delete=models.CASCADE, db_column='user_id')
    call_time = models.CharField(max_length=128)
    description = models.TextField()

    class Meta:
        db_table = 'history'

    def __str__(self):
        return self.call_time


class SaleSessionModel(models.Model):
    start_time = models.DateTimeField(null=True)
    last_update = models.DateTimeField(null=True)
    close_time= models.DateTimeField(null=True)
    customer_id = models.PositiveIntegerField(null=False)
    created_by = models.PositiveIntegerField(null=True)
    stage_id = models.IntegerField(null=True)
    status = models.CharField(max_length=64, null=True, blank=True)

    class Meta:
        db_table = 'sale_session'

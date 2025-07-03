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
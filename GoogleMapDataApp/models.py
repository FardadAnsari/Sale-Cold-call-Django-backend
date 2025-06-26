from django.db import models

class GoogleMapModel(models.Model):
    last_update = models.DateTimeField()
    shop_id_company = models.CharField(max_length=128, unique=True)
    shop_url_company = models.CharField(max_length=512, null=True, blank=True)
    shop_name = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.CharField(max_length=128, null=True, blank=True)
    longitude = models.CharField(max_length=128, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    plus_code = models.CharField(max_length=255, null=True, blank=True)
    postcode = models.CharField(max_length=128, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0, null=True, blank=True)
    total_reviews = models.IntegerField(null=True, blank=True)
    website = models.CharField(max_length=1024, null=True, blank=True)
    search_txt = models.CharField(max_length=128, null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    is_open_now = models.BooleanField(null=True, blank=True)
    opening_hours = models.JSONField(null=True, blank=True)
    provider_url = models.CharField(max_length=1024, null=True, blank=True)
    providers = models.JSONField(null=True, blank=True)
    services = models.CharField(max_length=512, null=True, blank=True)

    class Meta:
        db_table = 'googlemaps'

    def __str__(self):
        return self.shop_name
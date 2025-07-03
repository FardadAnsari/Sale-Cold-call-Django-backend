from rest_framework import serializers
from .models import HistoryModel



class HistoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryModel
        fields = '__all__'

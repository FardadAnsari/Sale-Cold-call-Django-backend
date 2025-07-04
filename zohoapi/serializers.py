from rest_framework import serializers


class OwnerSerializer(serializers.Serializer):
    email = serializers.EmailField()


class TagSerializer(serializers.Serializer):
    name = serializers.CharField()
    id = serializers.CharField()


class LeadDataSerializer(serializers.Serializer):
    Owner = OwnerSerializer(required=False)
    Tag = TagSerializer(many=True, required=False)

    Company = serializers.CharField(required=False, allow_blank=True)
    Last_Name = serializers.CharField(required=True)
    First_Name = serializers.CharField(required=False, allow_blank=True)
    Email = serializers.EmailField(required=False, allow_blank=True)
    Description = serializers.CharField(required=False, allow_blank=True)

    Internet_Connection_Status = serializers.CharField(required=False, allow_blank=True)
    Premises_Condition = serializers.CharField(required=False, allow_blank=True)
    Land_Line_Provider = serializers.CharField(required=False, allow_blank=True)
    Land_Line_Type = serializers.CharField(required=False, allow_blank=True)


class FeatureExecutionSerializer(serializers.Serializer):
    name = serializers.CharField()


class ZohoLeadSerializer(serializers.Serializer):
    data = serializers.ListField(
        child=LeadDataSerializer(),
        required=True
    )
    apply_feature_execution = serializers.ListField(
        child=FeatureExecutionSerializer(),
        required=False,
        default=[]
    )
    skip_feature_execution = serializers.ListField(
        child=FeatureExecutionSerializer(),
        required=False,
        default=[]
    )
    trigger = serializers.ListField(
        child=serializers.CharField(),
        required=False,
        default=[]
    )

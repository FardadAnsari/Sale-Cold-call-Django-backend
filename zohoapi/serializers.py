from rest_framework import serializers


class OwnerSerializer(serializers.Serializer):
    email = serializers.EmailField()


class TagSerializer(serializers.Serializer):
    name = serializers.CharField()
    id = serializers.CharField()


class LeadDataSerializer(serializers.Serializer):
    Owner = OwnerSerializer(required=False)
    Tag = TagSerializer(many=True, required=False)

    Company = serializers.CharField(required=True, allow_blank=False)
    Previous_Name = serializers.CharField(required=False, allow_blank=True)
    Company_Registered_Name=serializers.CharField(required=False, allow_blank=True)
    Phone=serializers.CharField(required=False, allow_blank=True)
    Phone_2=serializers.CharField(required=False, allow_blank=True)
    First_Name = serializers.CharField(required=False, allow_blank=True)
    Last_Name = serializers.CharField(required=True)
    Mobile=serializers.CharField(required=False, allow_blank=True)
    Email = serializers.EmailField(required=False, allow_blank=True)
    Website=serializers.CharField(required=False, allow_blank=True)
    Lead_Status=serializers.CharField(required=False, allow_blank=True)
    stage=serializers.CharField(required=False, allow_blank=True)
    Lead_Source=serializers.CharField(required=False, allow_blank=True)
    Industry=serializers.CharField(required=False, allow_blank=True)
    Sales_Participants=serializers.CharField(required=False, allow_blank=True)
    Area=serializers.CharField(required=False, allow_blank=True)
    Interest_Rate=serializers.CharField(required=False, allow_blank=True)
    Last_Caller=serializers.CharField(required=False, allow_blank=True)
    Next_Follow_Up=serializers.CharField(required=False, allow_blank=True)
    Lead_Owner=serializers.CharField(required=False, allow_blank=True)
    Street=serializers.CharField(required=False, allow_blank=True)
    City_Pick_List=serializers.CharField(required=False, allow_blank=True)
    State=serializers.CharField(required=False, allow_blank=True)
    Zip_Code=serializers.CharField(required=False, allow_blank=True)
    Country=serializers.CharField(required=False, allow_blank=True)
    Latitude=serializers.CharField(required=False, allow_blank=True)
    Longitude=serializers.CharField(required=False, allow_blank=True)
    Description = serializers.CharField(required=True, allow_blank=True)
    Internet_Connection_Status = serializers.CharField(required=True, allow_blank=True)
    Master_Socket_To_Counter=serializers.CharField(required=False, allow_blank=True)
    Premises_Condition=serializers.CharField(required=False, allow_blank=True)
    Business_Start_Date=serializers.DateField(required=False)
    Has_Kitchen_Printer=serializers.BooleanField(required=False)
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

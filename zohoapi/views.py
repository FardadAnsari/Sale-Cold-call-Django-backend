import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ZohoLeadSerializer


class ZohoAccountsExporter:
    def __init__(self, client_id, client_secret, refresh_token):
        self.client_id = client_id
        self.client_secret = client_secret
        self.refresh_token = refresh_token
        self.access_token = self._get_access_token()

    def _get_access_token(self):
        url = "https://accounts.zoho.eu/oauth/v2/token"
        params = {
            "refresh_token": self.refresh_token,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "refresh_token"
        }

        response = requests.post(url, params=params)
        response.raise_for_status()
        return response.json().get("access_token")

    def create_lead_record(self, lead_data):
        url = "https://www.zohoapis.eu/crm/v3/Leads/upsert"
        headers = {
            "Authorization": f"Zoho-oauthtoken {self.access_token}",
            "Content-Type": "application/json"
        }

        payload = {
            "data": lead_data.get("data"),
            "apply_feature_execution": lead_data.get("apply_feature_execution", []),
            "skip_feature_execution": lead_data.get("skip_feature_execution", []),
            "trigger": lead_data.get("trigger", [])
        }

        response = requests.post(url, headers=headers, json=payload)
        try:
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError:
            print(f"❌ Failed to create lead: {response.text}")
            raise

class CreateZohoLeadView(APIView):
    serializer_class = ZohoLeadSerializer

    def post(self, request):
        serializer = ZohoLeadSerializer(data=request.data)
        if serializer.is_valid():
            client_id = "1000.VRPJQPM9K4QABZX0I1UMYV4VFJ15SU"
            client_secret = "c83aff8e09e1880580d9db4268c1402d10be4dd867"
            refresh_token = "1000.5186732c29ad0e5589e26ea9d8325e3c.8890ee1a080e988f8f8a4ab14c8ce589"

            zoho_exporter = ZohoAccountsExporter(client_id, client_secret, refresh_token)
            try:
                result = zoho_exporter.create_lead_record(serializer.validated_data)
                return Response(result, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"error": f"Failed to create lead in Zoho: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
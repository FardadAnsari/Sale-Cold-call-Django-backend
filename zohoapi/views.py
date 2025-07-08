import requests
import logging

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

logger = logging.getLogger(__name__)


class ZohoAccountsExporter:
    def __init__(self):
        self.client_id = "1000.VRPJQPM9K4QABZX0I1UMYV4VFJ15SU"
        self.client_secret = "c83aff8e09e1880580d9db4268c1402d10be4dd867"
        self.refresh_token = "1000.be5ffcc266343e30324c709ffc2720a4.40b5ab8a46744d89c28aa8b0ece24581"
        self.access_token = self._get_access_token()

    def _get_access_token(self):
        url = "https://accounts.zoho.eu/oauth/v2/token"
        params = {
            "refresh_token": self.refresh_token,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "refresh_token"
        }

        logger.info(f"🔑 Fetching Zoho access token")
        response = requests.post(url, params=params)
        try:
            response.raise_for_status()
            access_token = response.json().get("access_token")
            logger.info(f"✅ Zoho access token received")
            return access_token
        except requests.exceptions.HTTPError:
            logger.error(f"❌ Zoho token error: {response.text}")
            raise

    def create_lead_record(self, lead_data):
        url = "https://www.zohoapis.eu/crm/v3/Leads/upsert"
        headers = {
            "Authorization": f"Zoho-oauthtoken {self.access_token}",
            "Content-Type": "application/json"
        }

        # 🔒 Force Tag to always have your fixed value
        for record in lead_data.get("data", []):
            record["Tag"] = [
                {
                    "name": "Onboareding Zone App",
                    "id": "458329000059988037"
                }
            ]

        payload = {
            "data": lead_data.get("data"),
            "apply_feature_execution": lead_data.get("apply_feature_execution", [{"name": "layout_rules"}]),
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
    """
    POST: Create or upsert a Zoho CRM lead record.
    """

    def post(self, request):
        logger.info(f"📥 Incoming lead data: {request.data}")

        zoho_exporter = ZohoAccountsExporter()
        try:
            result = zoho_exporter.create_lead_record(request.data)
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception("❌ Error while creating Zoho lead record")
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

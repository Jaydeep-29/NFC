from rest_framework import serializers
from nfc_app.models import NFC_Details  

class NFC_DetailSerializer(serializers.ModelSerializer):
   class Meta:
       model = NFC_Details
       fields = '__all__'
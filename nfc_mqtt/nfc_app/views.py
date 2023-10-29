import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import NFC_Details
from .serializers import NFC_DetailSerializer
import json
from rest_framework import status


# Create your views here.
class nfc_detail(APIView):
    print("--------home called----------")
    
    def get (self,request):
        nfc_detail = NFC_Details.objects.all()
        serializer = NFC_DetailSerializer(nfc_detail, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        try:
            print("---------post method--------",request.method,request.data ) 
            req = json.loads(request.data)
            uid = req['UID']   
            latitude = req['latitude']   
            longitude = req['longitude']   
            nfc_obj = NFC_Details.objects.create(uid=uid,latitude=latitude,longitude=longitude)
            nfc_obj.save()
            Res = {"Status":status.HTTP_200_OK,"Message":"Successful",}
            print("--------res-------",Res)
            return Response(Res)
            # return Response(json.dumps(Res))
        except Exception as e:
            print("------------exception ----------",e)
            Res = {"Status":status.HTTP_500_INTERNAL_SERVER_ERROR,}
            return Response(Res)
        
        
from email import message
from msilib.schema import Class
from turtle import pd
from django.shortcuts import render
from .serializers import serializers
from .models import Data
from .serializers import Dataserializer
import json
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class AssignmentAPI(APIView):
    def post(self,request,*args,**kwargs):
        json_data=request.data
        temp=json.dumps(json_data)
        pdata=json.loads(temp)
        Data=Dataserializer(data=pdata)
        if Data.is_valid():
            Data.save()
            message={'id':pdata['id'],'Message':pdata['message'],'Created_at':datetime.now(),'Updated_at':datetime.now(),"Created_By":{"id":pdata['id'],"Username":pdata['Username'],"Email":pdata['email']}}
            return Response(message)


        else:
            message={'Message':"There is some error while you fill the form Please enter the Message correctly ","Error":Data.errors}
            return Response(message)

        

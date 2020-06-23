from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
import json

from secrets import FIREBASE_TOKEN
from article.models import User


class ReqView(APIView):

    def post(self, request):
         
        open_url = request.body.decode('utf-8').trim()

        url = "https://fcm.googleapis.com/fcm/send"

        user = User.objects.get(pk=1)

        data = {
            "to": user.token,
            "data": {
                "url": open_url
            },
            "android": {
                "ttl": "10s"
            }
        }

        headers = {
            'Authorization': 'key='+FIREBASE_TOKEN,
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data = json.dumps(data))

        print(response.text.encode('utf8'))

        return Response("looks like success")
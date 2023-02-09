from django.shortcuts import render

# Create your views here.
from requests import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class ItemView(APIView):
    def get(self, request: Request, item_id):
        return render(request, 'api/item.html', context={"item_id": item_id})


from django.shortcuts import render

# Create your views here.
from requests import Request
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Item


class ItemView(APIView):
    def get(self, request: Request, item_id):
        item = get_object_or_404(Item, id=item_id)
        return render(request, 'api/item.html', context={"item": item})


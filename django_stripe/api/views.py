import stripe
import dotenv
from os import environ
from django.shortcuts import render
from django.urls import reverse
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Item
from .utils import create_item_buy_session

dotenv.load_dotenv()

# For using in html templates
public_stripe_key = environ.get("public_stripe_key")

# For making api calls
secret_stripe_key = environ.get("secret_stripe_key")

if public_stripe_key is None:
    raise KeyError("Define your public_stripe_key in .env file")

if secret_stripe_key is None:
    raise KeyError("Define your secret_stripe_key in .env file")

stripe.api_key = secret_stripe_key


class ItemView(APIView):
    def get(self, request, item_id):
        item = get_object_or_404(Item, id=item_id)
        url_to_buy_item = reverse("buy_item", args=[item_id])

        return render(
            request=request,
            template_name='api/item.html',
            context={
                "item": item,
                "buy_url": url_to_buy_item,
                "stripe_key": public_stripe_key
            }
        )


class BuyView(APIView):
    def get(self, request, item_id):
        item = get_object_or_404(Item, id=item_id)

        session = create_item_buy_session(item)
        return Response(data={"session_id": session.id})

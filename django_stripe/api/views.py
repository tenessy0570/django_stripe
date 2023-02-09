import stripe

from django.shortcuts import render
from django.urls import reverse
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Item

stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"


class ItemView(APIView):
    def get(self, request, item_id):
        item = get_object_or_404(Item, id=item_id)
        url_to_buy_item = reverse("buy_item", args=[item_id])

        return render(request, 'api/item.html', context={"item": item, "buy_url": url_to_buy_item})


class BuyView(APIView):
    def get(self, request, item_id):
        item = get_object_or_404(Item, id=item_id)

        session: stripe.checkout.Session = stripe.checkout.session.Session.create(success_url="https://vk.com", mode="payment", line_items=[
            {"price": stripe.Price.create(
                unit_amount=item.price * 100,
                currency="usd",
                recurring=None,
                product=stripe.Product.create(name=item.name)
            ),
                "quantity": 1
            }
        ])
        return Response(data={"session_id": session.id})

import stripe

from . import models


def create_item_buy_session(item: models.Item) -> stripe.checkout.Session:
    product = stripe.Product.create(name=item.name)
    price = stripe.Price.create(
        unit_amount=item.price * 100,  # From cents to dollars
        currency="usd",
        recurring=None,
        product=product
    )

    session = stripe.checkout.session.Session.create(
        success_url="https://vk.com",
        mode="payment",
        line_items=[
            {
                "price": price,
                "quantity": 1
            }
        ]
    )
    return session

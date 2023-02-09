from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('item/<int:item_id>', views.ItemView.as_view(), name="get_item")
]

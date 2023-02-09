from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    description = models.TextField(
        null=False,
        blank=False
    )
    price = models.IntegerField(null=False, blank=False)

    class Meta:
        verbose_name = "Item"

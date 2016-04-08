from django.db import models
from oscar.apps.partner.abstract_models import AbstractStockRecord

from uwkmdemo.meta import AbstractClassWithoutFieldsNamed as without


class StockRecord(without(AbstractStockRecord, 'partner_sku')):
    henk = models.NullBooleanField()
    partner_sku = models.CharField("Partner SKU", max_length=1280)


from oscar.apps.partner.models import *  # noqa

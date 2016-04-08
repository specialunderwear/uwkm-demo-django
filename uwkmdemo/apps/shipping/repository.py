from oscar.apps.shipping.repository import Repository as _Repository
from oscar.apps.shipping import methods as shipping_methods


class Repository(_Repository):
    methods = (shipping_methods.FixedPrice(10000, 11000),)

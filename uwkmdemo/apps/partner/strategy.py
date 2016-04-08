from decimal import Decimal
from oscar.apps.partner.strategy import Default
from oscar.apps.partner.prices import FixedPrice


class Henk(Default):
    def pricing_policy(self, product, stockrecord):
        # Check stockrecord has the appropriate data
        return FixedPrice(
            currency=stockrecord.price_currency,
            excl_tax=Decimal(1000),
            tax=Decimal('0.00')
        )


class Selector(object):
    """
    Responsible for returning the appropriate strategy class for a given
    user/session.

    This can be called in three ways:

    #) Passing a request and user.  This is for determining
       prices/availability for a normal user browsing the site.

    #) Passing just the user.  This is for offline processes that don't
       have a request instance but do know which user to determine prices for.

    #) Passing nothing.  This is for offline processes that don't
       correspond to a specific user.  Eg, determining a price to store in
       a search index.

    """

    def strategy(self, request=None, user=None, **kwargs):
        """
        Return an instanticated strategy instance
        """
        # Default to the backwards-compatible strategy of picking the first
        # stockrecord but charging zero tax.
        return Henk(request)

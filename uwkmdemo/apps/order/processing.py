import logging
from oscar.apps.order.processing import EventHandler as _EventHandler


logger = logging.getLogger(__name__)


class EventHandler(_EventHandler):
    def handle_order_status_change(self, order, new_status, note_msg=None):
        logger.info("Order %s changed status to %s" % (order, new_status))
        super(EventHandler, self).handle_order_status_change(order, new_status, note_msg)

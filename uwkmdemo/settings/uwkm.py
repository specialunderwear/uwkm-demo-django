from oscar.defaults import *
WAGTAIL_SITE_NAME = 'henk'

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

OSCAR_DASHBOARD_NAVIGATION[5]['children'] += [{
    'label': 'Ga naar het cms',
    'url_name': 'wagtailadmin_home',
}]
OSCAR_DASHBOARD_DEFAULT_ACCESS_FUNCTION = 'uwkmdemo.access.access_fn'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

OSCAR_INITIAL_ORDER_STATUS = 'new'

OSCAR_ORDER_STATUS_PIPELINE = {
    'new': ('pending',),
    'pending': ('paid',),
    'paid': ('completed',),
    'completed': ()
}

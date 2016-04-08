from oscar.defaults import *

WAGTAIL_SITE_NAME = 'henk'

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}
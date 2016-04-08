import os

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': os.environ.get('DJANGO_LOGLEVEL', 'INFO'),
        'handlers': ['console', 'mail_admins'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(name)s %(message)s',
        },
        'simple': {
            'format': '[%(asctime)s] %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
        },
    },
    'loggers': {
        'uwkmdemo': {
            'level': 'DEBUG',
            'propagate': True
        },
        'oscar': {
            'propagate': True
        },
        'django': {
            'propagate': True,
        },
        'django.db': {
            'level': 'WARNING'
        },
        # Django loggers
        'django.request': {
            'level': 'ERROR',
            'propagate': False
        },
    }
}

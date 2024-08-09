import sys

from logging_settings.log_filters import DebugWarningLogFilter, CriticalLogFilter, ErrorLogFilter

'''
    [Статус]
    В работе
    [Описание скрипта]
    Конфигурационный файл логирования  
    [Исполнители]
    Alexandr153
'''

logging_config = {
    'version': 1,
    'disable_existing_loggers': True,


    'formatters': {
        'default': {
            'format': '#%(levelname)-8s %(name)s:%(funcName)s - %(message)s'
        },
        'main_formatter': {
            'format': '#{levelname} [{asctime}] {filename}:'
                      '{lineno} - {name} - {message}',
            'style': '{'
        }
    },


    'filters': {
        'critical_filter': {
            '()': CriticalLogFilter,
        },
        'error_filter': {
            '()': ErrorLogFilter,
        },
        'debug_warning_filter': {
            '()': DebugWarningLogFilter,
        }
    },


    'handlers': {
        'default': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        },
        'stderr': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        },
        'stdout': {
            'class': 'logging.StreamHandler',
            'formatter': 'main_formatter',
            'stream': sys.stdout
        }
        # 'error_file': {
        #     'class': 'logging.FileHandler',
        #     'filename': 'error.log',
        #     'mode': 'w',
        #     'level': 'DEBUG',
        #     'formatter': 'formatter_1',
        #     'filters': ['error_filter']
        # },
        # 'critical_file': {
        #     'class': 'logging.FileHandler',
        #     'filename': 'critical.log',
        #     'mode': 'w',
        #     'formatter': 'formatter_3',
        #     'filters': ['critical_filter']
        # }
    },


    'loggers': {
        '__main__': {
            'level': 'DEBUG',
            'handlers': ['stdout'],
            'propagate': False
        },
        'core.handlers.interface.commands_menu.support': {
            'level': 'DEBUG',
            'handlers': ['stdout'],
            'propagate': False
        },
        'core.states.states': {
            'level': 'DEBUG',
            'handlers': ['stdout'],
            'propagate': False
        }
    },


    'root': {
        'formatter': 'default',
        'handlers': ['default']
    }
}

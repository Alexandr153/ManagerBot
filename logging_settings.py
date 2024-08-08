import sys

from log_filters import DebugWarningLogFilter, CriticalLogFilter, ErrorLogFilter

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
        'formatter_1': {
            'format': '[%(asctime)s] #%(levelname)-8s %(filename)s:'
                      '%(lineno)d - %(name)s:%(funcName)s - %(message)s'
        },
        'formatter_2': {
            'format': '#%(levelname)-8s [%(asctime)s] - %(filename)s:'
                      '%(lineno)d - %(name)s:%(funcName)s - %(message)s'
        },
        'formatter_3': {
            'format': '#%(levelname)-8s [%(asctime)s] - %(message)s'
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
            'formatter': 'formatter_2',
            'filters': ['debug_warning_filter'],
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
        'core.handlers.interface.commands_menu.support': {
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

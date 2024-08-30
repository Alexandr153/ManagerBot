import logging

'''
    [Статус]
    Своевременные дополнения
    [Описание скрипта]
    Фильтры для логов
    [Исполнители]
    Alexandr153
'''


class ErrorLogFilter(logging.Filter):
    def filter(self, record):
        return record.levelname == 'ERROR'


class DebugWarningLogFilter(logging.Filter):
    def filter(self, record):
        return record.levelname in ('DEBUG', 'WARNING')


class CriticalLogFilter(logging.Filter):
    def filter(self, record):
        return record.levelname == 'CRITICAL'

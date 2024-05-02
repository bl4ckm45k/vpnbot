import logging

import requests


class CustomFormatter(logging.Formatter):
    def __init__(self):
        super().__init__(fmt="%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s")


class APINotificationHandler(logging.Handler):
    def __init__(self, token, admin):
        logging.Handler.__init__(self)
        self.url = f'https://api.telegram.org/bot{token}/sendMessage'
        self.admin = admin
        self.formatter = CustomFormatter()

    def emit(self, record):
        log_entry = self.format(record)
        log_entry = log_entry.replace('[', '\n[')
        log_entry = log_entry.replace(']', ']\n')
        log_entry = log_entry.replace('__ -', '__ -\n')
        payload = {'chat_id': self.admin,
                   'text': f'<code>{log_entry}</code>',
                   'parse_mode': 'HTML'}
        requests.post(self.url, json=payload)

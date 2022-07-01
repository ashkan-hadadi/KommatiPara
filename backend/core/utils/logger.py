import json
import logging
from datetime import datetime


class APIFilter(logging.Filter):
    def filter(self, record):
        return True


class JSONFormatter(logging.Formatter):
    time_format = "%Y-%m-%dT%H:%M:%S.%fZ"

    @staticmethod
    def format_message(record):
        return {
            'request': {
                'time': datetime.fromtimestamp(record.created).isoformat(),
                'path': record.request.url.path,
                'headers': dict(record.request.headers),
                'params': dict(record.request.query_params),
                'body': record.request.state.body
            },
            'response': {
                'status_code': record.response.status_code,
                'headers': dict(record.response.headers)
            }
        }

    def format(self, record):
        message = self.format_message(record)
        return json.dumps(message, default=str, ensure_ascii=False)

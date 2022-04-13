from datetime import datetime

class DateConverter:
    regex = '\d{4}-\d{2}-\d{2}T\d{2}-\d{2}'
    format = '%Y-%m-%dT%H-%M'

    def to_python(self, value):
        return datetime.strptime(value, self.format)

    def to_url(self, value):
        return value.strftime(self.format)

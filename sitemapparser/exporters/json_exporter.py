from json import dumps
from ..exporter import Exporter


class JSONExporter(Exporter):
    short_name = 'json'

    def export_sitemaps(self):
        return dumps(list(sm.__dict__ for sm in self.data.get_sitemaps()))

    def export_urls(self):
        return dumps(list(u.__dict__ for u in self.data.get_urls()))

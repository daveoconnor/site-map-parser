import csv
import io
from ..exporter import Exporter


class CSVExporter(Exporter):
    short_name = 'csv'

    def export_sitemaps(self):
        buffer = io.StringIO()
        writer = csv.DictWriter(
            buffer,
            delimiter=",",
            fieldnames=['loc', 'lastmod'],
            quoting=csv.QUOTE_NONNUMERIC
        )
        writer.writeheader()
        for sm in self.data.get_sitemaps():
            writer.writerow(sm.__dict__)

        return buffer.getvalue().rstrip()

    def export_urls(self):
        buffer = io.StringIO()
        writer = csv.DictWriter(
            buffer,
            delimiter=",",
            fieldnames=['loc', 'lastmod', 'changefreq', 'priority'],
            quoting=csv.QUOTE_NONNUMERIC
        )
        writer.writeheader()
        for url in self.data.get_urls():
            writer.writerow(url.__dict__)

        return buffer.getvalue().rstrip()

import csv
import io
from ..exporter import Exporter
from ..url import Url
from ..sitemap import Sitemap


class CSVExporter(Exporter):
    short_name = 'csv'

    def export_sitemaps(self):
        buffer = io.StringIO()
        writer = csv.DictWriter(
            buffer,
            delimiter=",",
            fieldnames=Sitemap.fields,
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
            fieldnames=Url.fields,
            quoting=csv.QUOTE_NONNUMERIC
        )
        writer.writeheader()
        for url in self.data.get_urls():
            writer.writerow(url.__dict__)

        return buffer.getvalue().rstrip()

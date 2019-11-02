from sitemapper.site_mapper_iterator import SiteMapperIterator
import logging
logger = logging.getLogger(__name__)


class SiteMapper:
    def __init__(self, url):
        self.wrapped = self.process_url(url)

    @staticmethod
    def process_url(url):
        logger.debug("_process_url: {}".format(url))
        return []

    def __iter__(self):
        return SiteMapperIterator(self.wrapped)

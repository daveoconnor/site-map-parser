import logging
from .url import Url


class UrlSet:
    allowed_fields = ['loc', 'lastmod', 'changefreq', 'priority']

    def __init__(self, urlset_element):
        self.urls = self.urls_from_url_set_element(urlset_element)

    @staticmethod
    def url_from_url_element(url_element):
        logger = logging.getLogger(__name__)
        logger.debug("urls_from_url_element {}".format(url_element))
        url_data = {}
        for ele in url_element:
            name = ele.xpath('local-name()')
            value = ele.xpath('text()')[0]
            if name in UrlSet.allowed_fields:
                url_data[name] = value

        logger.debug("url_data {}".format(url_data))
        return Url(**url_data)

    @staticmethod
    def urls_from_url_set_element(url_set_element):
        logger = logging.getLogger(__name__)
        logger.debug("urls_from_url_set_element {}".format(url_set_element))

        for url_element in url_set_element:
            yield UrlSet.url_from_url_element(url_element)

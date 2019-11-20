import pytest
from datetime import datetime
from lxml import etree
from io import BytesIO
from sitemapparser.url_set import UrlSet
from sitemapparser.url import Url
from unittest.mock import MagicMock


class TestUrlSet:
    def setup(self):
        url_set_data_bytes = open('tests/urlset_a.xml', 'rb').read()
        utf8_parser = etree.XMLParser(encoding='utf-8')
        self.url_set_data_xml = etree.parse(BytesIO(url_set_data_bytes), parser=utf8_parser)
        self.url_set_element = self.url_set_data_xml.getroot()
        self.url_element_1 = self.url_set_data_xml.getroot()[0]
        self.url_element_2 = self.url_set_data_xml.getroot()[1]

    def test_allowed_fields(self):
        for f in UrlSet.allowed_fields:
            assert f in ['loc', 'lastmod', 'changefreq', 'priority']

    def test_url_from_url_element(self):
        url = UrlSet.url_from_url_element(self.url_element_1)
        assert isinstance(url, Url)
        assert url.loc == 'http://www.example.com/page/a/1'
        assert type(url.lastmod) is datetime
        assert str(url.lastmod) == '2005-01-01 00:00:00'
        assert url.changefreq == 'monthly'
        assert url.priority == 0.8

    def test_urls_from_url_set_element(self):
        urls = UrlSet.urls_from_url_set_element(self.url_set_element)
        assert len(list(urls)) == 3

    def test_init(self):
        u = UrlSet(self.url_set_element)
        assert len(list(u.urls)) == 3

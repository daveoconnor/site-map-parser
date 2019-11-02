import pytest
from unittest.mock import Mock
import requests
import requests_mock
from sitemapper.data_helpers import download_uri_data, data_to_element


def test_download_uri_data_sitemap_index():
    with requests_mock.mock() as m:
        smi_data = open('sitemapper/tests/sitemap_index_data.xml', 'rb').read()
        m.get('http://www.example.com/sitemapindex.xml', content=smi_data)
        downloaded_data = download_uri_data('http://www.example.com/sitemapindex.xml')
        assert downloaded_data == smi_data


def test_download_uri_data_urlset():
    with requests_mock.mock() as m:
        us_data = open('sitemapper/tests/urlset_a.xml', 'rb').read()
        m.get('http://www.example.com/urlset_a.xml', content=us_data)
        downloaded_data = download_uri_data('http://www.example.com/urlset_a.xml')
        assert downloaded_data == us_data


def test_data_to_element_sitemap_index():
    smi_data = open('sitemapper/tests/sitemap_index_data.xml', 'rb').read()
    root_element = data_to_element(smi_data)
    assert len(root_element.xpath("/*[local-name()='sitemapindex']")) == 1
    assert len(root_element.xpath("/*[local-name()='urlset']")) == 0


def test_data_to_element_sitemap_index_broken():
    smi_data = open('sitemapper/tests/sitemap_index_data_broken.xml', 'rb').read()
    with pytest.raises(SyntaxError):
        root_element = data_to_element(smi_data)
    # assert len(root_element.xpath("/*[local-name()='sitemapindex']")) == 1
    # assert len(root_element.xpath("/*[local-name()='urlset']")) == 0


def test_data_to_element_urlset():
    us_data = open('sitemapper/tests/urlset_a.xml', 'rb').read()
    root_element = data_to_element(us_data)
    assert len(root_element.xpath("/*[local-name()='sitemapindex']")) == 0
    assert len(root_element.xpath("/*[local-name()='urlset']")) == 1


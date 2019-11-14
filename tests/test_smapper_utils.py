from sitemapparser.smapper_utils import uri_modifier, get_args
import argparse

def test_uri_modifier_begins():
    test_url1 = 'example.com'
    assert uri_modifier(test_url1) == 'http://example.com/sitemap.xml'
    test_url2 = 'http://www.example.com'
    assert uri_modifier(test_url2) == 'http://www.example.com/sitemap.xml'


def test_uri_modifier_ends():
    test_url1 = 'http://www.example.com'
    assert uri_modifier(test_url1) == 'http://www.example.com/sitemap.xml'
    test_url2 = 'http://www.example.com/'
    assert uri_modifier(test_url2) == 'http://www.example.com/sitemap.xml'
    test_url3 = 'http://www.example.com/sitemap.xml'
    assert uri_modifier(test_url3) == 'http://www.example.com/sitemap.xml'


def test_get_args_long():
    sys_argv = [
        'http://www.example.com',
        '--log',
        'DEBUG',
        '--exporter',
        'json'
    ]
    (url, logging_level, exporter_format) = get_args(sys_argv)
    assert url == 'http://www.example.com'
    assert logging_level == 'DEBUG'
    assert exporter_format == 'json'


def test_get_args_default():
    sys_argv = [
        'http://www.example.com',
    ]
    (url, logging_level, exporter_format) = get_args(sys_argv)
    assert url == 'http://www.example.com'
    assert logging_level == 'INFO'
    assert exporter_format == 'csv'

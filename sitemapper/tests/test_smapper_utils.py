import pytest
from unittest import mock
from smapper_utils import uri_modifier, get_args
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


@mock.patch('argparse.ArgumentParser.parse_args',
            return_value=argparse.Namespace(
                url='http://www.example.com',
                logging_level='DEBUG'
            ))
def test_get_args_long(mock_args):
    (url, logging_level) = get_args()
    assert url == 'http://www.example.com'
    assert logging_level == 'DEBUG'

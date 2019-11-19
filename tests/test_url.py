from datetime import datetime
import pytest
from sitemapparser.url import Url


class TestUrl:
    def test_init_fully_loaded(self):
        u = Url(
            loc='http://www.example2.com/index2.html',
            lastmod='2010-11-04T17:21:18+00:00',
            changefreq='never',
            priority='0.3',
        )
        assert u.loc == 'http://www.example2.com/index2.html'
        assert type(u.lastmod) is datetime
        assert str(u.lastmod) == '2010-11-04 17:21:18+00:00'
        assert u.changefreq == 'never'
        assert u.priority == '0.3'

    def test_str(self):
        s = Url(loc='http://www.example2.com/index2.html')
        assert str(s) == 'http://www.example2.com/index2.html'

import logging
logger = logging.getLogger(__name__)


class SitemapIndex:
    def __init__(self, loc, lastmod=None):
        self.loc = loc
        self.lastmod = lastmod

    def __str__(self):
        return self.loc

class Url:
    fields = 'loc', 'lastmod', 'changefreq', 'priority'

    def __init__(self, loc, lastmod=None, changefreq=None, priority=None):
        """
        Representation of the <url> element
        :param loc: String, URL of the page.
        :param lastmod: DateTime, The date of last modification of the file.
        :param changefreq: String, How frequently the page is likely to change.
        :param priority: String, The priority of this URL relative to other URLs on your site.
        """
        self.loc = loc
        self.lastmod = lastmod
        self.changefreq = changefreq
        self.priority = priority

        # TODO: restrict changefreq to
        #    always
        #    hourly
        #    daily
        #    weekly
        #    monthly
        #    yearly
        #    never
        # TODO: convert lastmod to be a DateTime object
        # TODO: confirm priority is a float between 0.0 to 1.0

    def __str__(self):
        return self.loc

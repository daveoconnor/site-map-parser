from .base_data import BaseData


class Url(BaseData):
    fields = 'loc', 'lastmod', 'changefreq', 'priority'
    valid_freqs = ('always', 'hourly', 'daily', 'weekly', 'monthly',
                   'yearly', 'never')

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

        # TODO: confirm priority is a float between 0.0 to 1.0

    @property
    def changefreq(self):
        return self._changefreq

    @changefreq.setter
    def changefreq(self, frequency):
        if frequency is not None and frequency not in Url.valid_freqs:
            error_msg = "'{}' is not an allowed value: {}"
            raise ValueError(error_msg.format(frequency, Url.valid_freqs))
        self._changefreq = frequency

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, priority):
        if priority is not None:
            priority = float(priority)
            if priority < 0.0 or priority > 1.0:
                raise ValueError("'{}' is not between 0.0 and 1.0")
        self._priority = priority

    def __str__(self):
        return self.loc

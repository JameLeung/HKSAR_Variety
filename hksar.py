#!/usr/bin/python
### BEGIN LICENSE
# Copyright (c) 2020, Jame Leung
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
### END LICENSE

"""
    Variety quote plugin sourcing quotes from hong kong web sites
    This script is placed in '~/.config/variety/plugins' and then activated from inside Variety's
    Preferences Quotes menu
"""

import logging
import random
import re
from locale import gettext as _
from variety.Util import Util
from variety.plugins.IQuoteSource import IQuoteSource
try:
    from urllib.request import Request, urlopen  # Python 3
except ImportError:
    from urllib2 import Request, urlopen         # Python 2
from bs4 import BeautifulSoup

logger = logging.getLogger("variety")

class HKSARSource(IQuoteSource):
    """
        Retrieves quotes from hong kong websites. Reads the last quotes.
        Attributes:
            quotes(list): list containing the quotes
    """

    def __init__(self):
        self.active = False
        super(IQuoteSource, self).__init__()
        self.quotes = []

    @classmethod
    def get_info(cls):
        return {
            "name": "Jame Leung - HKSAR web sites news ",
            "description": _("Real Time News from Hongkong RSS feed\n"
                             "DIY in COVID19 stage"),
            "author": "Jame Leung",
            "url": "https://github.com/JameLeung/HKSAR_Variety",
            "version": "0.0.1"
        }

    def supports_search(self):
        return False

    def activate(self):
        if self.active:
            return
        self.active = True
        self.quotes = []
        self.fetch_hksar_news()

    def deactivate(self):
        self.quotes = []
        self.active = False

    def is_active(self):
        return self.active

    def fetch_hksar_news(self):
    hksar_url=["https://rthk.hk/rthk/news/rss/c_expressnews_clocal.xml","https://rthk.hk/rthk/news/rss/c_expressnews_cgreaterchina.xml","https://rthk.hk/rthk/news/rss/c_expressnews_cinternational.xml", "https://rthk.hk/rthk/news/rss/c_expressnews_cfinance.xml", "https://rthk.hk/rthk/news/rss/c_expressnews_csport.xml", "https://www.scmp.com/rss/91/feed", "https://www.scmp.com/rss/2/feed", "https://www.scmp.com/rss/4/feed", "https://www.scmp.com/rss/3/feed", "https://www.scmp.com/rss/5/feed", "http://news.on.cc/ncnews/rss/loc_news.xml", "https://www.inmediahk.net/rss.xml", "https://www.thestandnews.com/rss/", "https://news.mingpao.com/rss/pns/s00001.xml", "http://rss.appleactionews.com/rss.xml"]

        select_url = a = hksar_url[randrange(len(hksar_url))]

        self.quotes = []

	for a in d.entries:

		author = d.feed.title.replace(" ","") + " " + str(format(a.published_parsed.tm_hour,"02d")) + ":" + str(format(a.published_parsed.tm_min,"02d"))
		
                self.quotes.append({
                    "quote": a.title.replace(" ","")
                    "author": author,
                    "sourceName": "HKSAR",
                    "link": a.link})

        if not self.quotes:
            logger.warning("Could not find quotes for URL " + vdm_url)

    def get_for_author(self, author):
        return []

    def get_for_keyword(self, keyword):
        return []

    def get_random(self):
        return self.quotes

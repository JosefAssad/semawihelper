#!/usr/bin/env python

import mwclient
from IPython import embed


class MWSite(object):

    def __init__(self):
        self.site = None
        self.connect()

    def connect(self):
        hostname = raw_input("Host: ")
        path = raw_input("Path: ")
        username = raw_input("User: ")
        password = raw_input("Pass: ")
        self.site = mwclient.Site(('http', hostname), path)
        self.site.login(username, password)

    def purge_page(self, page_title):
        """Executes a purge action on page_title.
        https://www.mediawiki.org/wiki/Manual:Purge
        
        Arguments:
        page_title: the MediaWiki page title to purge
        """
        self.site.pages[page_title].purge()

    def nulledit_page(self, page_title, summary):
        page = self.site.Pages[page_title]
        text = page.text()
        page.save(text, summary=summary)
        print "Page %s nulledited." % (page_title)

    def nulledit_category(self, category_name, summary):
        """Useful for those times when a template has changed and purge doesn't
        help.

        Arguments:
        category_name: the MediaWiki category of pages to purge        
        summary:       recentchanges summary message
        """
        progress = 1
        for page in self.site.Pages['Kategori:'+category_name]:
            print "nulledit_category: %s" % (progress)
            self.nulledit_page(page.page_title, summary)
            progress += 1
        
    def list_category(self, category):
        for page in self.site.Pages['Kategori:'+category]:
            print "Page: %s" % (page.page_title)

    def nuke_category(self, category):
        for page in self.site.Pages['Kategori:'+category]:
            print "deleting %s..." % (page.page_title)
            page.delete()
        catpage_also = raw_input("Delete [[Category:%s]] also? y/n:" % (category))
        if catpage_also == "y":
            self.site.Pages["Category:%s" % (category)].delete()

    def rename_property(self, oldname, newname):
        """for renaming semantic properties

        Arguments:
        oldname: The current property name
        newname: The desired property name

        """
        pass

if __name__ == '__main__':
    site = MWSite()
    embed()

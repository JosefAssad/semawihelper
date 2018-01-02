#!/usr/bin/env python

import mwclient
import sys
from IPython import embed

class MWSite(object):

    
    def __init__(self):
        self.site = None
        self.connect()

    def connect(self):
        hostname = input("Host:")
        path = input("Path:")
        username = input("User:")
        password = input("Pass:")
        self.site = mwclient.Site((hostname), path)
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
        print("Page %s nulledited." % (page_title))

    def nulledit_category(self, category_name, summary):
        """Useful for those times when a template has changed and purge doesn't
        help.

        Arguments:
        category_name: the MediaWiki category of pages to purge        
        summary:       recentchanges summary message
        """
        progress = 1
        for page in self.site.Pages['Kategori:'+category_name]:
            print("nulledit_category: %s" % (progress))
            self.nulledit_page(page.page_title, summary)
            progress += 1
        
    def list_category(self, category):
        for page in self.site.Pages['Kategori:'+category]:
            print("Page: %s" % (page.page_title))

    def list_category2(self, category):
        for page in self.site.Pages['Kategori:'+category]:
            a = (page.page_title)
            list += [a]
        return list

    def allcategories(self):
        """Retrieve all categories on the wiki as a generator."""
        return self.allpages()

    
    def nuke_category(self, category):
        for page in self.site.Pages['Kategori:'+category]:
            print("deleting %s..." % (page.page_title))
            page.delete()
        catpage_also = raw_input("Delete [[Category:%s]] also? y/n:" % (category))
        if catpage_also == "y":
            self.site.Pages["Category:%s" % (category)].delete()

    @property
    def pages(self):
        """return a list of all the pages on the site"""
        allpageslist =[]
        for page in site.site.Pages: 
            allpageslist.append(page.page_title)
        return allpageslist

    def list_allpages():
        allpageslist =[]
        for page in site.site.Pages: 
            allpageslist.append(page.page_title)
        return allpageslist

    def rename_property(self, oldname, newname):
        """for renaming semantic properties
        Arguments:
        oldname: The current property name
        newname: The desired property name
        """
        list = []
        list = site.list_allpages() 
        i = 0
        # Loop.
        for item in list:
        # check inside the page as a string
            print(str(list[i]))
            #x=site.site.Pages[page].text()
            i +=1
    
if __name__ == '__main__':
    site = MWSite()
    embed()
    



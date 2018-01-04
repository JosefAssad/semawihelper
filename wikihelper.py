#!/usr/bin/env python

import mwclient
import sys
from IPython import embed

class MWSite(object):

    
    def __init__(self):
        self.site = None
        self.connect()
        self.rename_all()
        

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
        catpage_also = input("Delete [[Category:%s]] also? y/n:" % (category))
        if catpage_also == "y":
            self.site.Pages["Category:%s" % (category)].delete()

    @property
    def pages(self):
        """return a list of all the pages on the site"""
        allpageslist =[]
        for page in site.site.Pages: 
            allpageslist.append(page.page_title)
        return allpageslist


    def see_pages(self):
        for page in site.site.Pages:
            print(page)
    
    def rename_property(self, oldname, newname):
        """for renaming semantic properties
        Arguments:
        oldname: The current property name
        newname: The desired property name
        """
        examinedpages = 0
        # Loop.
        #go through all pages and replace:
        for page in site.site.Pages:
            text = page.text()
            text = text.replace(oldname, newname)
            page.save(text, summary='Changed value of '+ oldname + ' to '+ newname)
            examinedpages +=1
        print("Done! "+str(examinedpages)+' were checked for '+str(oldname))

    def rename_all(self):
        print('Wikihelper at Your service')
        oldname = input('Please write the current property you would like to change: ')
        newname = input('Now write the desired property to take its place: ')
        print('Attention! All occurrances of '+str(oldname)+'will be replaced with '+str(newname))
        accept = input('Do you wish to continue? Y/N')
        if accept == 'y':
            self.rename_property(oldname, newname)
        

        
if __name__ == '__main__':
    site = MWSite()
    embed()
    



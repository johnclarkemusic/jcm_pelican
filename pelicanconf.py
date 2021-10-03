#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'John H. Clarke'
SITENAME = 'JohnClarkeMusic.com'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = 'simple-jcm-1.0'  

OUTPUT_PATH = 'docs'  

# STATIC_PATHS = ['static']

DISQUS_SITENAME = 'johnclarkemusic'
TWITTER_USERNAME= 'johnclarkemusic'
MENUITEMS= [("Blog",  '' )]
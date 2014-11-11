#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'seudo'
SITENAME = u'LoveLive! 學園偶像祭'
SITEURL = 'http://seudo.github.io/llsif_tw/'
STATIC_PATHS = ["images", ]

PATH = 'content'
TIMEZONE = 'Asia/Taipei'
DEFAULT_LANG = u'zh-tw'
DEFAULT_DATE_FORMAT =  '%Y-%m-%d %a'
DEFAULT_PAGINATION = 10

THEME = 'theme'
PLUGIN_PATHS = ['plugins']
PLUGINS = []

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('日版非官方wiki', 'http://lovelive.sakura.ne.jp/wiki/'),
        ('日版非官方wiki','http://www59.atwiki.jp/lovelive-sif/'),
        ('譜面影片', 'http://www.nicovideo.jp/mylist/36769914'),
        )

# Social widget
SOCIAL = (('github', 'http://github.com/seudo'),
         )
GOOGLE_ANALYTICS = 'UA-55911875-1'
TWITTER_USERNAME = "736575646f"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

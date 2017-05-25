#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

AUTHOR = 'Fluid'
SITENAME = 'Blog de Fluid'
SITEURL = 'https://lordjhony.github.io'

PATH = 'content'

TIMEZONE = 'America/Bogota'

DEFAULT_LANG = 'Spanish'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Formating URLs
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

# Plugins
PLUGIN_PATHS = 'pelican-plugins'
PLUGINS = ['asciidoc_reader','assets','neighbors','share_post','related_posts','disqus_static']

# Discus
DISQUS_SITENAME = 'https://lordjhony.github.io'
DISQUS_SECRET_KEY = 'OYR1s5hqatldqUzAw8nllRMrQZfzHYcSSFwsCWmedwzpEU6OjVi5kx4jOWRDArAF'
DISQUS_PUBLIC_KEY = '6y2rWTTNCXtOa74qKQK8Laz3YKz4JzV9ClXSeGYchXDfEhtImJqyrrSwfWjY8Scs'

# theme
THEME = "theme/pelican-clean-blog"


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

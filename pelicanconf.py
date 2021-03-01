#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Mário N Jhunior'
SITEURL = ''
SITENAME = "{'devjhunior'}  | Notas de um desenvolvedor"
SITETITLE = "{'devjhunior'}"
SITESUBTITLE = "notas de um desenvolvedor"
SITEDESCRIPTION = "devjhunior | notas de um desenvolvedor"
BROWSER_COLOR = "#333333"


PATH = 'content'

STATIC_PATHS = [
    'pages',
    'images',
    'articles',
    'images/favicon.ico',
]

EXTRA_PATH_METADATA = {
    'images/favicon.ico': {'path': 'favicon.ico'},
}

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'en'
THEME = 'themes/flex'

I18N_TEMPLATES_LANG = "en"
DEFAULT_LANG = "en"
OG_LOCALE = "en_US"
LOCALE = "en_US"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = False
HOME_HIDE_TAGS = True

# Blogroll
# LINKS = (('Pelican', 'https://getpelican.com/'),
#          ('Python.org', 'https://www.python.org/'),
#          ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'https://github.com/devjhunior'),
          ('linkedin', 'https://www.linkedin.com/in/marionascimentojunior'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

USE_LESS = True
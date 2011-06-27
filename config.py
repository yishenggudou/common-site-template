# -*- coding: utf-8 -*-
import os.path as op
import settings

'''Config for grappelli'''
GRAPPELLI_ADMIN_TITLE = "Site administration"

'''Config for filebrowser'''

# The absolute path to the directory that holds the media-files you want to browse
FILEBROWSER_MEDIA_ROOT = settings.MEDIA_ROOT
# URL that handles the media served from MEDIA_ROOT
FILEBROWSER_MEDIA_URL = settings.MEDIA_URL
# Main FileBrowser Directory. Leave empty in order to browse all files and folders within MEDIA_ROOT
FILEBROWSER_DIRECTORY = ''
# The URL and Path to your FileBrowser media-files
FILEBROWSER_URL_FILEBROWSER_MEDIA = settings.STATIC_URL + 'filebrowser/'
FILEBROWSER_PATH_FILEBROWSER_MEDIA = op.join(settings.STATIC_ROOT, 'filebrowser/')

# API keys

from django.contrib import settings

# TinyMCE
TINYMCE_JS_URL = settings.STATIC_URL + 'js/tiny_mce/tiny_mce_src.js'
TINYMCE_JS_ROOT = settings.STATIC_ROOT + 'js/tiny_mce'
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace",
    'theme': "advanced",
}
TINYMCE_SPELLCHECKER = True
TINYMCE_COMPRESSOR = True

# API keys

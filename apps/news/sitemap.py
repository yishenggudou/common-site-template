from django.contrib.sitemaps import Sitemap
from news.models import NewsPost

class NewsSitemap(Sitemap):
    #location = "/news/"
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return NewsPost.objects.filter(is_draft=False)

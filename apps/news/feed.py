from django.contrib.syndication.views import Feed
from news.models import NewsPost

class LatestNewsFeed(Feed):
    title = "Latest News"
    link = "/news/"
    description = "News updates."

    def items(self):
        return NewsPost.objects.order_by('-pub_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

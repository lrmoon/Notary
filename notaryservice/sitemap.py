from django.contrib import sitemaps
from django.urls import reverse

class StaticViewsSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "weekly"

    def items(self):
        return ['main_app:home']
    
    def location(self, item):
        return self.request.build_absolute_uri(reverse(item))
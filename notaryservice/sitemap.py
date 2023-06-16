from django.contrib import sitemaps
from django.urls import reverse

class StaticViewsSitemap(sitemaps.Sitemap):
    protocol = 'https'
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return ['main_app:home']
    
    def location(self, item):
        return reverse(item)
    
    

from django.contrib import sitemaps
from django.urls import reverse

class StaticViewsSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "weekly"

    def items(self):
        return ['main_app:home']
    
    def location(self, item):
        return reverse(item)
    
    def get_urls(self, site=None, **kwargs):
        urls = []
        for item in self.paginator.page_range:
            url = reverse('main_app:home')
            urls.append(
                {
                    'location': url,
                    'priority': self.priority,
                    'changefreq': self.changefreq
                }
            )
        return urls
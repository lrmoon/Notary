from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from .sitemap import StaticViewsSitemap





sitemaps = {
    'sitemap': StaticViewsSitemap,
}



urlpatterns = [
    path('', include('main_app.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'), #this is straight from docs
    path('robots.txt', include('robots.urls')),
    path('admin/', admin.site.urls),
]

from django.urls import path
from django.contrib.sitemaps.views import sitemap
from .sitemap import StaticViewsSitemap
from django.contrib.sites.models import Site


from . import views

app_name = 'main_app'

sitemaps = {
    'sitemap': StaticViewsSitemap,
}


urlpatterns = [
    path('', views.home, name='home'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'), #this is straight from docs
    
] 

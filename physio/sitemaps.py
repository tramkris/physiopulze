from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
            return ['home','contactus','aboutus','treatmentsoffered',
                'backpain','jointpain','neckpain','headaches',
                'strainssprains','sportsinjury','orthorehabilitation',
                'neurorehabilitation']

    def location(self, item):
        return reverse(item)

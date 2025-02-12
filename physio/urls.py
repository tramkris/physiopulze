
from django.contrib import admin
from django.urls import path, include
from . import views
from physio.views import contact, success

# Added for Sitemap changes
from django.contrib.sitemaps.views import sitemap
from physio.sitemaps import StaticSitemap

# Added for robots.txt changes
from django.views.generic.base import TemplateView

sitemaps={
    'static': StaticSitemap
}

urlpatterns = [
    path('', views.home, name='home'),
    path('contact-us', views.contactus, name='contactus'),
    path('about-us', views.aboutus, name='aboutus'),
    path('treatments-offered', views.treatmentsoffered, name='treatmentsoffered'),
    path('treatments-offered/back-pain', views.backpain, name='backpain'),
    path('treatments-offered/joint-pain', views.jointpain, name='jointpain'),
    path('treatments-offered/neck-pain', views.neckpain, name='neckpain'),
    path('treatments-offered/head-aches', views.headaches, name='headaches'),
    path('treatments-offered/strains-sprains', views.strainssprains, name='strainssprains'),
    path('treatments-offered/sports-injury', views.sportsinjury, name='sportsinjury'),
    path('treatments-offered/ortho-rehabilitation', views.orthorehabilitation, name='orthorehabilitation'),
    path('treatments-offered/neuro-rehabilitation', views.neurorehabilitation, name='neurorehabilitation'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'),
    path('failure/', views.failure, name='failure'),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}),
    path('robots.txt/', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"))
]

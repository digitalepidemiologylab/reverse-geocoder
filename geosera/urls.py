from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'geosera.views.home', name='home'),
    # url(r'^geosera/', include('geosera.foo.urls')),

     url(r'reverse/(-?\d+\.\d+),(-?\d+\.\d+)$', 'geosera.views.reverse.reverse', name='reverse'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

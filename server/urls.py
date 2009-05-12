from django.conf.urls.defaults import *
from django.conf import settings


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^server/', include('server.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    (r'^ash/bulk-add-tags/$', 'server.returnsongs.views.bulk_add_tags'),
    (r'^ash/tags-added/$', 'server.returnsongs.views.tags_added'),
    (r'^ash/retrievesongs/$', 'server.returnsongs.views.retrievesongs'),
    (r'^songs/(?P<path>.*)$', 'django.views.static.serve', 
        {'document_root': settings.STATIC_DOC_ROOT}),
    (r'^mymedia/(?P<path>.*)', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),



)

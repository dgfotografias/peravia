from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Peravia.views.home', name='home'),
    # url(r'^Peravia/', include('Peravia.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^', include('agenda.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^encuestas/', include('polls.urls', namespace='polls')),
    url(r'^', include(admin.site.urls)),

    (r'', include('django.contrib.auth.urls')),
    url(r'^chaining/', include('smart_selects.urls')),

)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
                            url(r'^static/(?P<path>.*)$', 'serve',{'document_root':settings.STATIC_ROOT}),
                            )
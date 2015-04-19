from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lazimlik.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'yonetim.views.anasayfa'),
    url(r'^isverelim$', 'yonetim.views.isverelim'),
    url(r'^isyapalim$', 'yonetim.views.isyapalim'),
)

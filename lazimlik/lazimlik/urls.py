from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lazimlik.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'yonetim.views.anasayfa', name='anasayfa'),
    url(r'^isverelim$', 'yonetim.views.isverelim', name='isverelim'),
    url(r'^isyapalim$', 'yonetim.views.isyapalim', name='isyapalim'),
    url(r'', include('social_auth.urls')),
    url(r'^login$', 'social_app.views.login', name='giris'),
    url(r'^logout/$', 'social_app.views.logout'),
)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
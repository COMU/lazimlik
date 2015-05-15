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
	url(r'^about/$', 'yonetim.views.about', name='about'),
	url(r'^about_user/$', 'yonetim.views.about_user', name='about_user'),
	url(r'^home/$', 'social_app.views.home', name='home'),
	url(r'^user/$', 'yonetim.views.user', name='user'),
	url(r'^isverelim/$', 'yonetim.views.isverelim', name='isverelim'),
	url(r'^isyapalim/$', 'yonetim.views.isyapalim', name='isyapalim'),
	url(r'^isyapalim_user/$', 'yonetim.views.isyapalim_user', name='isyapalim_user'),
	url(r'', include('social_auth.urls')),
	url(r'^login/$', 'social_app.views.login', name='login'),
	url(r'^logout/$', 'social_app.views.logout', name='logout'),
	url(r'^is_al/$', 'yonetim.views.is_al', name='is_al'),
	url(r'^results/$', 'yonetim.views.results', name='results'),
	url(r'^search/$', 'yonetim.views.search', name='search'),
)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
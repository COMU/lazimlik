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
	url(r'^user/$', 'yonetim.views.profil_olustur', name='user'),
	url(r'^userdetail/$', 'yonetim.views.userdetail', name='userdetail'),
	url(r'^isverelim/$', 'yonetim.views.is_olustur', name='isverelim'),
	url(r'^is_goruntule/$', 'yonetim.views.is_goruntule', name='is_goruntule'),
	url(r'^isyapalim_user/$', 'yonetim.views.isyapalim_user', name='isyapalim_user'),
	url(r'^alinan_isler/$', 'yonetim.views.alinan_isler', name='alinan_isler'),
	url(r'^is_havuzu/$', 'yonetim.views.is_havuzu', name='is_havuzu'),
	url(r'^teslim_edildi/$', 'yonetim.views.teslim_edildi', name='teslim_edildi'),
	url(r'^teslim_edilen_is/$', 'yonetim.views.teslim_edilen_is', name='teslim_edilen_is'),
	url(r'', include('social_auth.urls')),
	url(r'^login/$', 'social_app.views.login', name='login'),
	url(r'^logout/$', 'social_app.views.logout', name='logout'),
	url(r'^is_al/(?P<is_id>[0-9]+)', 'yonetim.views.is_al', name='is_al'),
	url(r'^is_teslim_et/(?P<is_id>[0-9]+)', 'yonetim.views.is_teslim_et', name='is_teslim_et'),
	url(r'^results/$', 'yonetim.views.results', name='results'),
	url(r'^search/$', 'yonetim.views.search', name='search'),
)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

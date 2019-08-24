
from django.conf.urls import url, include
from django.contrib import admin
from main_app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^(?P<pk>\d+)/detail/$',views.detail,name='detail'),
    url(r'^main_app/',include('main_app.urls')),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^search/',views.search,name='search_view'),
    url(r'^search2/',views.search2,name='search_view2'),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^update/',views.update_profile,name='update'),
    url(r'^rests/',views.rest_list,name='rests'),
    url(r'^hots/',views.hot_list,name='hots'),
    url(r'^tops/',views.toprated,name='tops'),
    url(r'^cafs/',views.caf_list,name='cafs'),
    url(r'^bars/',views.bar_list,name='bars'),
    url(r'^books/',views.bookmarks,name='books'),
    url(r'^books2/',views.bookmarks2,name='books2'),
    url(r'^remove/',views.remove_bk,name='remove'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

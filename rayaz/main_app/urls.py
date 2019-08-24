from django.conf.urls import url
from django.contrib.auth.views import logout,login
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


app_name = 'main_app'

urlpatterns = [
    url(r'^signup/',views.signup,name='signup'),
    url(r'^logout',logout, {'next_page': '/'},name='logout'),
    url(r'^login/',login, {'template_name':'main_app/login.html'}, name='login'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

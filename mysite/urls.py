from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from matchmaker.views import HomePageView
from accounts.views import register_view, login_view, logout_view


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^register/$', register_view, name='register'),
    url(r'^messages/', include('django_messages.urls')),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^login/$', login_view, name='login'),
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^profile/', include("matchmaker.urls", namespace='profiles')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.conf.urls import url, include
from .views import home, single


urlpatterns = [
    url(r'^home/(?P<id>\d+)/$', single, name='question_single'),
    url(r'^home/$', home, name='question_home'),

]
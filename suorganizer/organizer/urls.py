from django.conf.urls import include, url
from django.contrib import admin

from organizer.views import tag_detail,tag_list,startup_list,startup_detail

urlpatterns = [
    # Examples:
    # url(r'^$', 'suorganizer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^startup/',startup_list,name='organizer_startup_list'),
    url(r'^startup/(?P<slug>[\w\-]+)/$',startup_detail,name='organizer_startup_detail'),
    url(r'^tag/$',tag_list,name='organizer_tag_list'),
    url(r'^tag/(?P<slug>[\w\-]+)/$',tag_detail,name="organizer_tag_detail"),
]

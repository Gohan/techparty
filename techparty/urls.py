from django.conf.urls import patterns, include, url
from techparty.wechat.views import TechpartyView

from django.contrib import admin
admin.autodiscover()

urlpatterns = \
    patterns('',
             url(r'^admin/', include(admin.site.urls)),
             url(r'^wechat/$', TechpartyView.as_view()),
             url(r'^reg_confirm/(?P<eid>\d+)/(?P<key>\w+)/$', 'techparty.website.views.confirm_event'),
             url(r'^lecturer/', include('techparty.lecturer.urls', namespace="lecturer")),
             url(r'^member/', include('techparty.member.urls', namespace="member")),
             url(r'^comments/', include('django.contrib.comments.urls')),
             )

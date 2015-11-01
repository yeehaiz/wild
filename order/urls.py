from django.conf.urls import include, url

from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'wild.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),

    url(r'^fill/$', views.fill),
    url(r'^submit/$', views.submit),
    url(r'^confirm/(\d+)/$', views.confirm),
    url(r'^cancel/(\d+)/$', views.cancel),
]

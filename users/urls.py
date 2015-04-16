from django.conf.urls import include, url

from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'wild.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),

    url(r'^login/$', views.login),
    url(r'^formlogin/$', views.formlogin),

]

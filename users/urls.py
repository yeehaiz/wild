from django.conf.urls import include, url

from users import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'wild.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),

    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^register/$', views.register),

    url(r'^verifycode/$', views.sendverifycode),
    url(r'^register/post/$', views.register_post),
    url(r'^register/check_username/$', views.register_check_username),

]

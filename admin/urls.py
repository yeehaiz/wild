from django.conf.urls import include, url

from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'wild.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),

    url(r'^events/$', views.events),
    url(r'^events/add/$', views.events_add),
    url(r'^events/update/(\d+)/$', views.events_update),
    url(r'^events/save/$', views.events_save),

    url(r'^uploadimage/$', views.uploadimage),

]

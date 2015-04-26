from django.conf.urls import include, url

from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'wild.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),

    url(r'^lists/$', views.lists),
    url(r'^lists2/$', views.lists2),
    url(r'^detail2/$', views.detail2),
    url(r'^detail/(\d+)/$', views.detail),

]

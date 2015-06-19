from django.conf.urls import include, url
#from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'wild.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', include('event.urls')),
    url(r'^user/', include('users.urls')),
    url(r'^event/', include('event.urls')),
    url(r'^order/', include('order.urls')),
    url(r'^admin/', include('admin.urls')),
    url(r'^mytest/', include('mytest.urls')),

]

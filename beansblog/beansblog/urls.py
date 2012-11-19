from django.conf.urls import patterns, include, url
import beansblog.views
import beansblog.admin.views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'beansblog.views.home', name='home'),
    url(r'^ueditor_imgup/$','beansblog.admin.views.ueditor_ImgUp'),
	url(r'^post_blog/$', 'beansblog.admin.views.post_blog'),
	url(r'^show_articles/$', 'beansblog.admin.views.show_articles'),
	# url(r'^beansblog/', include('beansblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'Blogsite.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^blogs/',
                           include('blogs.urls', namespace="blogs")),

                       url(r'^admin/', include(admin.site.urls)),
                       )

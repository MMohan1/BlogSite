from django.conf.urls import patterns, url

from blogs import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^add/$', views.addblock, name='addblock'),
                       # ex: /polls/5/
                       url(r'^(?P<blog_id>\d+)/$',
                           views.detail, name='detail'),
                       # ex: /polls/5/results/
                       url(r'^(?P<blog_id>\d+)/results/$',
                           views.results, name='results'),
                       # ex: /polls/5/vote/
                       url(r'^(?P<blog_id>\d+)/vote/$',
                           views.vote, name='vote'),
                       )

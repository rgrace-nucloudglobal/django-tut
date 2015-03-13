from django.conf.urls import patterns, url
from polls import views

urlpatterns = patterns('',
                       # ex: /polls/ - regex capturing that nothing is
                       # specified after /polls/
                       # url(r'^$', views.index, name='index'),
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       
                       # ex: /polls/5/ - regex capturing integer question_id
                       # parameter
                       # url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
                       url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
                       # ex: /polls/5/results/ - regex capturing a request for
                       # a given questions result page
                       # url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
                       url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
                       
                       # url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote')
                       url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote')
                       )

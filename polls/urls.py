from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/questions/
    url(r'^(?P<question_id>[0-9]+)/questions/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^isuseravailable/$', views.checkUserAvailability, name='isuseravailable'),
    url(r'^isemailnotregistered/$', views.checkEmailAvailability, name='isemailnotregistered'),
    url(r'^addquestion/$',views.addquestion,name='addquestion'),

    #url(r'^404/$', views.handler404, name='handler404'),
]
handler404 = 'polls.views.handler404'
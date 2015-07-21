from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^show_all/$',views.show_all,name='show_all'),
    url(r'^show_emp_with_code/$',views.show_emp_with_code,name='show_emp_with_code'),
    url(r'^show_emp_with_nthsalary/$',views.show_emp_with_nthsalary,name='show_emp_with_nthsalary'),
]
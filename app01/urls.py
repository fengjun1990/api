from app01.views import test,account,coursedetail
from django.conf.urls import url

urlpatterns = [
    url(r'^test/', test.test),
    url(r'^login/$', account.LoginView.as_view()),
    url(r'^reg/$', account.RegView.as_view()),

    url(r'^coursedetail/$', coursedetail.CourseDetailView.as_view({'get':'list'})),
    url(r'^coursedetail/(?P<pk>\d+)/$', coursedetail.CourseDetailView.as_view({'get':'retrieve'})),

    # url(r'^course/$', coursedetail.CourseView.as_view({'get':'list'})),
    url(r'^course/$', coursedetail.CourseView.as_view()),
]









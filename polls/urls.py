from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

from polls.serializers import QuestionList, QuestionDetail, ChoiceDetail, UserCreate, UserDetail
from . import views

urlpatterns = [
                  # Regular Django Views
                  url(r'^$', login_required(views.index), name='index'),
                  url(r'^(?P<pk>[0-9]+)/$', login_required(views.Detail.as_view()), name='detail'),
                  url(r'^(?P<pk>[0-9]+)/results/$', login_required(views.Results.as_view()), name='results'),
                  url(r'^(?P<question_id>[0-9]+)/vote/$', login_required(views.vote), name='vote'),

                  # API views
                  url(r'^api/questions/$', QuestionList.as_view(), name="api_questions"),
                  url(r'^api/questions/(?P<pk>[0-9]+)/$', QuestionDetail.as_view()),
                  url(r'^api/choices/(?P<pk>[0-9]+)/$', ChoiceDetail.as_view()),
                  url(r'^api/create_user/$', UserCreate.as_view()),
                  url(r'^api/users/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

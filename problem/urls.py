from django.urls import path
from problem.views import QuestionRetriveupdateDeleteView
from problem.views import QuestionCreateView

urlpatterns = [
    path("assesment/<int:pk>/questions/",QuestionCreateView.as_view()),

    path("questions/<int:pk>/",QuestionRetriveupdateDeleteView.as_view())
]
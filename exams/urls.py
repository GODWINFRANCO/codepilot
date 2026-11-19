from django.urls import path

from rest_framework.authtoken.views import ObtainAuthToken

from exams.views import AssessmentListView,AssessmentCreateView,AssesmentRetrieveUpdateDeleteView

urlpatterns=[
    # route to assessment list view
    path('assesment/all/',AssessmentListView.as_view()),
    # route to assessment create view
    path('assesment/add/',AssessmentCreateView.as_view()),
    # route to token authentication
    path('token/',ObtainAuthToken.as_view()),
    # route to assessment retrieve,update,delete view
    path('assesment/<int:pk>/',AssesmentRetrieveUpdateDeleteView.as_view()),
]
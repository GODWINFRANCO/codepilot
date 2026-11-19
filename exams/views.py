from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions,authentication
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView,CreateAPIView

from exams.serializers import AssesmentSerializer
from exams.models import Assesment
from accounts.models import User
from exams.permissions import IsOwner

from datetime import datetime,timedelta

# Create your views here.

class AssessmentListView(ListAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = AssesmentSerializer
    queryset = Assesment.objects.all()

# class AssesmentListCreateView(APIView):

#     authentication_classes=[authentication.TokenAuthentication]

#     permission_classes=[permissions.IsAuthenticated]

#     def get(self,request):

#         qs=Assesment.objects.filter(createdby=request.user)

#         serializer_instance = AssesmentSerializer(qs,many=True)

#         return Response(data=serializer_instance.data)

class AssessmentCreateView(CreateAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    serializer_class = AssesmentSerializer

    def perform_create(self, serializer):

        serializer.save(createdby=self.request.user)

        
    # def post(self,request):

    #     form_data = request.data

    #     serializer_instance = AssesmentSerializer(data=form_data)

    #     if serializer_instance.is_valid():

    #         start_time = serializer_instance.validated_data['starttime']

    #         duration = serializer_instance.validated_data['duration']

    #         start = datetime.combine(datetime.today(), start_time)

    #         end = start + timedelta(minutes=duration)

    #         serializer_instance.save(
    #             createdby=request.user,
    #             endtime=end.time()
    #         )

    #         return Response(data=serializer_instance.data)

    #     else:

    #         return Response(data=serializer_instance.errors)

class AssesmentRetrieveUpdateDeleteView(APIView):

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAdminUser]

    def get(self,request,pk=None):

        instance = get_object_or_404(Assesment,id=pk)

        self.check_object_permissions(request,instance)

        serializer_instance = AssesmentSerializer(instance)

        return Response(data=serializer_instance.data)

    def put(self,request,pk=None):

        instance = get_object_or_404(Assesment,id=pk)

        self.check_object_permissions(request,instance)

        form_data = request.data

        serializer_instance = AssesmentSerializer(data=form_data,instance=instance)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.validated_data)
        
        else:

            return Response(data=serializer_instance.errors)

    def delete(self,request,pk=None):

        instance = get_object_or_404(Assesment,id=pk)

        self.check_object_permissions(request,instance)

        instance.delete()

        return Response(data={"message":"deleted"})
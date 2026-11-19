from rest_framework import serializers

from datetime import datetime

from exams.models import Assesment

from problem.models import Question

from django.db.models import Sum

from problem.serializers import QuestionSerializer

class AssesmentSerializer(serializers.ModelSerializer):

    greetings = serializers.SerializerMethodField(read_only=True)
    
    question_count = serializers.SerializerMethodField(read_only=True)

    total_marks = serializers.SerializerMethodField(read_only=True)

    questions = serializers.SerializerMethodField(read_only=True)

    class Meta:

        model=Assesment

        fields = "__all__"

        read_only_fields = ["id","endtime","createdby"]

    def validate(self,validated_data):

        examdate = validated_data.get("examdate")
        
        if examdate<datetime.today().date():
            
            raise serializers.ValidationError("Please enter a valid examdate")
        
        return validated_data

    def get_greetings(self,obj):
        
        return "good morning"
    
    def get_question_count(self,obj):
    
        return Question.objects.filter(assessment=obj).count()

    def get_total_marks(self,obj):

        return Question.objects.filter(assessment=obj).values("score").aggregate(total=sum("score")).get("total")

    # def get_total_marks(self,obj):

    #     return Question.objects.filter(assessment=obj).aggregate(total=Sum("score"))["total"] or 0
    
    def get_total_marks(self, obj):
        
        total = Question.objects.filter(assessment=obj).aggregate(total=Sum("score"))["total"]
        
        return total or 0
    

    def get_questions(self,obj):

        question_objects = Question.objects.filter(assessment=obj)

        serializer_instance = QuestionSerializer(question_objects,many=True)

        return serializer_instance.data

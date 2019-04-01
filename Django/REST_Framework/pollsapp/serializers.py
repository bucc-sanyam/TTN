from rest_framework import serializers
from pollsapp.models import Questions, Choices

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
            model = Questions
            fields = ('question_text','pub_date','owner')

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choices
fields = ('question','choice_text','votes','owner')
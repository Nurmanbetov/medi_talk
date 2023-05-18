from rest_framework import serializers
from .models import Patient, Record, ConversationAI


class PatientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Patient
        fields = 'first_name'

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):

    records = RecordSerializer(many=True)

    class Meta:
        model = Patient
        fields = '__all__'
    

class ConversationSerializer(serializers.ModelSerializer):

    user = PatientSerializer()

    class Meta:
        model = ConversationAI
        fields = ['patient', 'text']

from rest_framework import serializers
from .models import Patient, Record, ConversationAI


class PatientSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Patient
        fields = 'first_name'
    

class ConversationSerializer(serializers.ModelSerializer):

    user = PatientSerializer()

    class Meta:
        model = ConversationAI
        fields = ['patient', 'text']

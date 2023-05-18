from rest_framework import serializers
from .models import Doctor, Patient, Record



class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):

    records = RecordSerializer(many=True)

    class Meta:
        model = Patient
        fields = '__all__'

from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from .serializers import ConversationSerializer
from .models import ConversationAI
from rest_framework.response import Response
from rest_framework import status
from .models import Patient, ConversationAI




class ChatAPI(RetrieveAPIView):
    
    serializer_class  = ConversationSerializer

    def post(self, request):
        if request.method == "POST":

            # print(request.data["user"])
            patient = Patient.objects.get(pk=int(request.data['user']))
            conversation = request.data['text']
            ConversationAI.objects.create(patient=patient, text=conversation)
            content = {'result': "Created!"}
            return Response(content ,status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
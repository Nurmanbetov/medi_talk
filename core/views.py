from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, APIView
from .serializers import ConversationSerializer
from .models import ConversationAI
from rest_framework.response import Response
from rest_framework import status
from .models import Patient, ConversationAI
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai


openai.api_key = os.getenv("OPENAI_API_KEY")


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

class ChatAPIMessage(APIView):
    def post(self, request):
        if request.method == "POST":
            messages = request.data['messages']
    
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            chat_response = completion.choices[0].message.content
            messages.append({"role": "assistant", "content": chat_response})
            return Response({"data": messages}, status=status.HTTP_200_OK)    
        return Response(status=status.HTTP_400_BAD_REQUEST)

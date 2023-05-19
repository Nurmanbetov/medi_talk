from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from .serializers import ConversationSerializer
from .models import ConversationAI
from rest_framework.response import Response
from rest_framework import status
from .models import Patient, ConversationAI
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai, json





class ChatAPI(RetrieveAPIView):
    
    """ Gets POST request, creates ConversationAI model, and saves it in datebase"""

    serializer_class  = ConversationSerializer

    def post(self, request):
        if request.method == "POST":

            patient = Patient.objects.get(pk=int(request.data['user']))
            conversation = request.data['text']
            ConversationAI.objects.create(patient=patient, text=conversation)
            content = {'result': "Created!"}
            return Response(content ,status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)

class ChatAPIMessage(APIView):

    """Gets POST request, ChatGPT generates and response been returned"""

    def post(self, request):
        if request.method == "POST":
            messages = json.loads(request.data)
            gptMessages = [item for item in messages]
            gptMessages[0]['content'] = 'Please provide me with your symptoms and medical history'
            gptMessages.insert(0, {"role": "user", "content": "let's play a role. you are my doctor and I'm your patient. ask me questions (in maximum 20 words)"})
            print(messages)
            for i, msg in enumerate(gptMessages):
                gptMessages[i]['content'] = gptMessages[i]['content'].replace('\n', '').replace('\'', '')
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=gptMessages
            )
            chat_response = completion.choices[0].message.content
            # chat_response = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'
            messages.append({"role": "assistant", "content": chat_response.replace('\'', '')})
            return Response(chat_response, status=status.HTTP_200_OK)    
        return Response(status=status.HTTP_400_BAD_REQUEST)

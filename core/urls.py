from django.urls import path 
from .views import ChatAPI, ChatAPIMessage


urlpatterns = [
    #path("<int:pk>/", ProfileRetrieveView.as_view(), name="profile"),
    path("create_conv/", ChatAPI.as_view(), name="chatAPI"),
    path("create_conv_message/", ChatAPIMessage.as_view(), name='chatAPIMessage')
]
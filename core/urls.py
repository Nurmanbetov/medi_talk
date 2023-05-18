from django.urls import path 
from .views import ChatAPI


urlpatterns = [
    #path("<int:pk>/", ProfileRetrieveView.as_view(), name="profile"),
    path("create_conv/", ChatAPI.as_view(), name="chatAPI")
]
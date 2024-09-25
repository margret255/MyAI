from django.urls import path
from . import views
urlpatterns=[
    path('',views.chatbot,name='chatbot'),
    path('',views.ask_openai,name='ask_openai')
]
# chat/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_view, name='chat_view'),
    path('ask/', views.ask_agent, name='ask_agent'),
]
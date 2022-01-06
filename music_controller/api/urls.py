from django.urls import path
from .views import RoomView, CreateRoomView

urlpatterns = [
    path('home', RoomView.as_view(), name='RoomView'),
    path('create-room', CreateRoomView.as_view())
]
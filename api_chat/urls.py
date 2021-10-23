from django.urls import path
from .views import GenericAPiView, SingleMessageAPiView, ListAPiView

urlpatterns = [
    path('api/', GenericAPiView.as_view()),
    path('api/messages/single/<int:id>/', SingleMessageAPiView.as_view()),
    path('api/messages/list/', ListAPiView.as_view()),
]

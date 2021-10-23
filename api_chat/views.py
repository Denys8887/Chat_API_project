from rest_framework import mixins, generics
from api_chat.models import Message
from api_chat.serializers import MessageSerializer


class GenericAPiView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin,
                     mixins.RetrieveModelMixin, ):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)


class SingleMessageAPiView(generics.GenericAPIView, mixins.ListModelMixin, mixins.UpdateModelMixin,
                           mixins.RetrieveModelMixin):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def put(self, request, id=None):
        return self.update(request, id)


class ListAPiView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

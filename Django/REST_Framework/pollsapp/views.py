from django.shortcuts import render
from .permissions import IsOwnerOrReadOnly, DidOwnerCreateQuestion
from .serializers import QuestionSerializer, ChoiceSerializer
from rest_framework import viewsets, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .models import Questions, Choices
from django.contrib.auth.models import User


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (permissions.IsAuthenticated,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choices.objects.all()
    serializer_class = ChoiceSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (permissions.IsAuthenticated, DidOwnerCreateQuestion,)

    def perform_create(self, serializer):
        # print(DidOwnerCreateQuestion(self.request).has_object_permission(self, Questions))
        # res = Questions.objects.get(id = int(self.request.POST['question']))
        # print(type(res.owner_id))
        # print(self.request.user)
        # print(dir(self.request.user))
        # print(type(self.request.user))
        # print(res.owner_id == self.request.user.id)
        # print(question.owner_id == request.user)
        serializer.save()


choices_list = ChoiceViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
choices_detail = ChoiceViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

question_list = QuestionViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
question_detail = QuestionViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
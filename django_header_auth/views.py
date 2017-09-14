from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ConsumerSerializer
from .models import Consumer


class ConsumerViewSet(viewsets.ModelViewSet):

    serializer_class = ConsumerSerializer
    lookup_field = 'uuid'

    def get_queryset(self):
        if self.request.user.is_staff:
            return Consumer.objects.all()
        return Consumer.objects.filter(pk=self.request.user.pk)

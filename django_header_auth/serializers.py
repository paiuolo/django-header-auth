from django.conf.urls import url, include
from rest_framework import serializers
from .models import Consumer


class ConsumerSerializer(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name')

    class Meta:
        model = Consumer
        fields = ('uuid', 'domain', 'email', 'date_joined', 'updated_at', 'classname', 'groups')
        read_only_fields = ('uuid', 'date_joined', 'token', 'updated_at', 'classname', 'groups')

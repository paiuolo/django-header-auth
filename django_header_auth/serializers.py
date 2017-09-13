from django.conf.urls import url, include
from rest_framework import serializers
from .models import Consumer


class ConsumerSerializer(serializers.ModelSerializer):
    uploads = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='uuid')

    groups = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name')

    class Meta:
        model = Consumer
        fields = ('uuid', 'domain', 'email', 'created_at', 'updated_at', 'classname', 'uploads', 'groups')
        read_only_fields = ('uuid', 'created_at', 'token', 'updated_at', 'classname', 'groups')

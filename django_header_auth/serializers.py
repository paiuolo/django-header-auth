from django.conf.urls import url, include
from rest_framework import serializers
from .models import Consumer


class ConsumerSerializer(serializers.HyperlinkedModelSerializer):
    groups = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name')

    class Meta:
        model = Consumer
        fields = ('url', 'uuid', 'domain', 'email',
                  'date_joined', 'updated_at', 'groups')
        read_only_fields = ('url', 'uuid', 'date_joined', 'token',
                            'updated_at', 'groups')
                            
        extra_kwargs = {
            'url': {'view_name': 'consumer-detail', 'lookup_field': 'uuid'}
        }

from dataclasses import field
from rest_framework import serializers
from hello.models import Destination


class DestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = "__all__"

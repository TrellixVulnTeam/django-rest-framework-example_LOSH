from rest_framework import serializers
from .models import Quickstart

class QuickstartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quickstart
        fields = ('id', 'name', 'paradigm', 'is_active', 'is_approved')
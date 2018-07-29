from django.shortcuts import render
from rest_framework import viewsets
from .models import Quickstart
from .serializers import QuickstartSerializer

# Create your views here.
class QuickstartView(viewsets.ModelViewSet):
    queryset = Quickstart.objects.all()
    serializer_class = QuickstartSerializer
    
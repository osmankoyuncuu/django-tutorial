from django.shortcuts import render
from .models import Tutorial
from .serailizer import TutorialSerializer
from rest_framework.viewsets import ModelViewSet

    
class Tutorials(ModelViewSet):

    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer

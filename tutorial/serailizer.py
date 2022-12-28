from rest_framework import serializers
from .models import Tutorial

class TutorialSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tutorial
        #fields = "__all__"
        fields = ["id","title", "description"]
        

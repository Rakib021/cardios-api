from rest_framework import serializers
from .models import Advocates

class AdvocateSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Advocates
    fields ='__all__'
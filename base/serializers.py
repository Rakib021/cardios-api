from rest_framework import serializers
from .models import Advocates ,Company

class AdvocateSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Advocates
    fields ='__all__'
    
    
class CompanySerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Company
    fields ='__all__'
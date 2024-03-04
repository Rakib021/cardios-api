from django.shortcuts import render,redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Advocates,Company
from rest_framework.views import APIView
from .serializers import AdvocateSerializer,CompanySerializer
from django.db.models import Q
from django.http import Http404


# Create your views here.
@api_view(["GET"])
def endpoints(request):
  data =['advocates','advocates/:username']
  
  return Response(data)

@api_view(["GET","POST"])
def advocates_list(request):
  if request.method == 'GET':
    query = request.GET.get('query')
    if query == None:
      query =''
      
    # username__icontains=query
    # this means if your are searching one thing then you forgot what things is it and you remember only firtrs three words then you have to search this 3 words
    advocates =Advocates.objects.filter(Q(username__icontains=query)| Q(bio__icontains=query))
    serializer = AdvocateSerializer(advocates,many=True)
    
    return Response(serializer.data)
  
  if request.method =='POST':
 
    advocate =Advocates.objects.create(username=request.data['username'],bio = request.data['bio'])
      
    serializer = AdvocateSerializer(advocate,many=False)
    context={'data':serializer.data}
    
    return Response(context)


  
class AdvocateDetail(APIView):
    def get_object(self, username):
        try:
            return Advocates.objects.get(username=username)
        except Advocates.DoesNotExist:
            raise Http404
  
    def get(self,request,username):
      advocate = self.get_object(username)
      serializer =AdvocateSerializer(advocate,many=False)
      return Response(serializer.data)
    
    def put(self,request,username):
      advocate = self.get_object(username)
      advocate.username = request.data['username']
      advocate.bio = request.data['bio']
      serializer =AdvocateSerializer(advocate,many=False)
      return Response(serializer.data)
    
    def delete(self,request,username):
      advocate = self.get_object(username)
      advocate.delete()
      return Response('User was deleted')
      

# @api_view(["GET","PUT","DELETE"])
# def advocates_detail(request,username):
#   advocate = Advocates.objects.get(username=username)
#   if request.method =='GET':
#     serializer =AdvocateSerializer(advocate,many=False)
#     return Response(serializer.data)
  
#   if request.method =='PUT':
#     advocate.username = request.data['username']
#     advocate.bio = request.data['bio']
    
#     advocate.save()
    
#     serializer = AdvocateSerializer(advocate,many=False)
#     print(serializer.data)
#     context={'data':serializer.data}
    
#     return Response(context)
  
  
#   if request.method =='DELETE':
#     advocate.delete()
#     return Response('User was deleted')


#for companies
@api_view(['GET'])
def companies_list(request):
  companies = Company.objects.all()
  serializer = CompanySerializer(companies,many=True)
  return Response(serializer.data)
  
  
  
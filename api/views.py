from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import EmployeeSerializer
from crm.models import Employees
from rest_framework.viewsets import ViewSet

class EmployeeListCreateView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Employees.objects.all()
        #deserialize
        #reference_name=serializerClass(query_set,many)
        serializer=EmployeeSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def post(self,request,*args,**kwargs):
        #serialization
        #reference_name=SerializerClass(data=request.data)
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    

class EmployeeMixinView(APIView):
    def get(self,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Employees.objects.get(id=id)
        serializer=EmployeeSerializer(qs,many=False)
        return Response(data=serializer.data)
    
    def put(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        employee_object=Employees.objects.get(id=id)
        serializer=EmployeeSerializer(data=request.data,instance=employee_object)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    
    
    
    def delete(self,*args,**kwargs):
        id=kwargs.get("pk")
        Employees.objects.get(id=id).delete()
        return Response(data={"message":"Employee delete"})
    
#...............viewsets..................#
class EmployeeViewSetView(ViewSet):
    def list(self,request,*args,**kwargs):
        qs=Employees.objects.all()
        serializer=EmployeeSerializer(qs,many=True)
        return Response(data=serializer.data)
    def create(self,request,*args,**kwargs):
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Employees.objects.get(id=id)
        serializer=EmployeeSerializer(qs)
        return Response(data=serializer.data)
    
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        employee_object=Employees.objects.get(id=id)
        serializer=EmployeeSerializer(data=request.data,instance=employee_object)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Employees.objects.get(id=id).delete()
        return Response(data={"message":"delete employee"})
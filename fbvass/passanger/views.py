from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Passanger
from .serializers import PassangerSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET','POST'])
def passanger_list(request):
    if request.method == 'GET':
        passangers = Passanger.objects.all()
        serializer = PassangerSerializer(passangers,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PassangerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def passanger_detail(request,pk):
    try:
        passanger = Passanger.objects.get(pk=pk)
    except Passanger.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PassangerSerializer(passanger)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PassangerSerializer(passanger,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        passanger.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



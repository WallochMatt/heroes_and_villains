from functools import partial
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PowerSerializer, SuperSerializer
from .models import Power, Super
from supers import serializers


# Create your views here.
@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':
        morality = request.query_params.get('type')
        supers = Super.objects.all()
        
        if morality:
            supers = supers.filter(super_type__type=morality)
            serializer = SuperSerializer(supers, many = True)
            return Response(serializer.data)
        else:
            custom_dictionary = {'heroes':[], 'villains': []}
            pk = 1
            for key in custom_dictionary: 
                temp = Super.objects.filter(super_type_id=pk)
                serializer = SuperSerializer(temp, many = True)
                custom_dictionary[key] = serializer.data
                pk += 1

            return Response(custom_dictionary, status=status.HTTP_200_OK)


    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)




@api_view(['GET', 'PUT', 'DELETE'])
def individual_super(request, pk):
    super = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(super)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['PATCH'])
def add_power_to_super(request, pk, set_power):
    new_power = Power.objects.get(id=set_power)
    super = get_object_or_404(Super, pk=pk)
    if request.method == 'PATCH': 
        super.power.add(new_power)
        serializer = SuperSerializer(super)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

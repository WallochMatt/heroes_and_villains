from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SuperType
from .serializers import SuperTypeSerializer



@api_view(['GET', 'POST'])
def types_list(request):
    if request.method == 'GET':
        types = SuperType.objects.all()
        serializer = SuperTypeSerializer(types, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SuperTypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)











@api_view(['GET', 'PUT', 'DELETE'])
def individual_type(requst, pk):
    type_of_super = get_object_or_404(SuperType, pk=pk)
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SuperSerializer
from .models import Super


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

        
        # heroes = supers.filter(super_type__type = 'Hero')
        # serializer = SuperSerializer(heroes, many=True)
        # return Response(serializer.data)
       
        else:#for supers.objects if super_type == 'hero'?
            custom_dictionary = {'heroes':[], 'villains': []}

            
            heroes = supers.filter(super_type__type = 'Hero')
            villains = supers.filter(super_type__type = 'Villain')
            
            for hero in heroes:
                serializer = SuperSerializer(heroes, many = True)
                custom_dictionary['heroes'] = serializer.data

            for villain in villains:
                serializer = SuperSerializer(villains, many = True)
                custom_dictionary['villains'] = serializer.data


            return Response(custom_dictionary)




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

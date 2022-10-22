from django.urls import is_valid_path
from rest_framework.response import Response
from rest_framework.decorators import api_view
from hello.models import Destination
from .serializers import DestSerializer


@api_view(['GET'])
def getData(request):
    # human = {"name": "shashank", "age": 24}
    destinations = Destination.objects.all()
    serializer = DestSerializer(destinations, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addData(req):
    serializer = DestSerializer(data=req.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print("NOTTTT")
    return Response(serializer.data)

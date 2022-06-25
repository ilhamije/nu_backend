from lapaks.models import Lapak
from lapaks.serializers import LapakSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class LapakList(APIView):
    """
    List all lapaks, or create a new snippet.
    """
    def get(self, request, format=None):
        lapaks = Lapak.objects.all()
        serializer = LapakSerializer(lapaks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LapakSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
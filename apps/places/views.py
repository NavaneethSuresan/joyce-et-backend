from rest_framework import generics, filters
from .serializers import PlaceSerializer
from django.http import JsonResponse
from .models import Place
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

class PlaceList(generics.ListAPIView):
    # Get all places, limit = 20
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category','id']
    search_fields = ['name', 'description']

    def get_paginated_response(self, data):
         return Response(data)
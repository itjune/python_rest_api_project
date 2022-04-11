from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from documents.models import Document
from documents.serializers import DocumentSerializer

class DocsList(ListCreateAPIView):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()



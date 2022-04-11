from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from django.forms import ValidationError

from documents.models import Document
from documents.serializers import DocumentListSerializer, DocumentCreateSerializer

class DocsList(ListCreateAPIView):
    queryset = Document.objects.all().values('slug').distinct()

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'POST':
            return DocumentCreateSerializer
        return DocumentListSerializer

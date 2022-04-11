from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView, 
    ListAPIView,
    RetrieveAPIView,
)
from django.forms import ValidationError

from documents.models import Document
from documents.serializers import (
    DocumentLatestSerializer,
    DocumentListSerializer, 
    DocumentCreateSerializer,
    DocumentRevisionsSerializer,
)

class DocsListView(ListCreateAPIView):
    queryset = Document.objects.all().values('slug').distinct()

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'POST':
            return DocumentCreateSerializer
        return DocumentListSerializer

class DocsRevisionsView(ListAPIView):
    serializer_class = DocumentRevisionsSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        docs = Document.objects.filter(slug=slug).all()
        return docs

class DocsLatestView(RetrieveAPIView):
    serializer_class = DocumentLatestSerializer
    lookup_field = 'slug'

    def get_object(self):
        slug = self.kwargs.get('slug')
        doc = Document.objects.filter(slug=slug).latest('revision')
        return doc

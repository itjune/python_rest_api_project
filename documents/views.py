from django.shortcuts import render
from django.http import Http404
from rest_framework.generics import (
    ListCreateAPIView, 
    ListAPIView,
    RetrieveAPIView,
)
from datetime import datetime

from documents.models import Document
from documents.serializers import (
    DocumentLatestSerializer,
    DocumentListSerializer, 
    DocumentCreateSerializer,
    DocumentRevisionsSerializer,
)
from documents.common import DateConverter

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
        if not docs:
            raise Http404("No such document")
        return docs

class DocsLatestView(RetrieveAPIView):
    serializer_class = DocumentLatestSerializer
    lookup_field = 'slug'

    def get_object(self):
        slug = self.kwargs.get('slug')
        try:
            doc = Document.objects.filter(slug=slug).latest('revision')
        except Document.DoesNotExist:
            raise Http404("No such document")
        return doc

class DocsRevisionView(RetrieveAPIView):
    serializer_class = DocumentLatestSerializer
    lookup_field = 'slug'

    def get_object(self):
        slug = self.kwargs.get('slug')
        timestamp_ = self.kwargs.get('revision')
        try:
            doc = Document.objects.filter(slug=slug, revision__lte=timestamp_).latest('revision')
        except Document.DoesNotExist:
            raise Http404("No such document")
        return doc

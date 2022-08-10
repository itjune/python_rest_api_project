from django.shortcuts import render
from django.http import Http404
from rest_framework.generics import (
    ListCreateAPIView, 
    ListAPIView,
    RetrieveAPIView,
)
from rest_framework import status
from rest_framework.response import Response
from datetime import datetime

from documents.models import Document
from documents.serializers import (
    DocumentLatestSerializer,
    DocumentListSerializer, 
    DocumentCreateSerializer,
    DocumentRevisionsSerializer,
    DocumentCreateRevisionSerializer,
)
from documents.common import DateConverter
from rest_framework.pagination import LimitOffsetPagination

class DocumetnsPagination(LimitOffsetPagination):
    default_limit = 10
    max_liimit = 20

class DocsListView(ListCreateAPIView):
    queryset = Document.objects.all().values('slug').distinct()
    pagination_class = DocumetnsPagination

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'POST':
            return DocumentCreateSerializer
        return DocumentListSerializer

class DocsRevisionsView(ListCreateAPIView):
    lookup_field = 'slug'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        docs = Document.objects.filter(slug=slug).all()
        if not docs:
            raise Http404("No such document")
        return docs

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'POST':
            return DocumentCreateRevisionSerializer
        return DocumentRevisionsSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['slug'] = kwargs.get('slug')
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

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

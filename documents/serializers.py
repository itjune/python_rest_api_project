from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from documents.models import Document

class DocumentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = ('slug', )

    
class DocumentCreateSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(
        max_length=50,
        validators=[UniqueValidator(queryset=Document.objects.values_list('slug', flat=True).distinct())]
    )

    class Meta:
        model = Document
        fields = ('slug', 'content')

class DocumentRevisionsSerializer(serializers.ModelSerializer):
    revision = serializers.DateTimeField(format="%Y-%m-%d %H:%M")

    class Meta:
        model = Document
        fields = ('revision', )


class DocumentCreateRevisionSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField()

    class Meta:
        model = Document
        fields = ('slug', 'content', 'revision')


class DocumentLatestSerializer(serializers.ModelSerializer):
    revision = serializers.DateTimeField(format="%Y-%m-%d %H:%M")

    class Meta:
        model = Document
        fields = ('slug', 'content', 'revision')

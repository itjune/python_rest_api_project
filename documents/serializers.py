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

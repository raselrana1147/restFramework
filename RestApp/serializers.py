from RestApp.models import Article
from rest_framework import serializers

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields=['id','title','description','author_name','created_at','updated_at']
    
    """_summary_

    Args:
        serializers (_type_): _description_

    Returns:
        _type_: _description_
  
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500)
    author_name = serializers.CharField(max_length=191)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    def create(self, validated_data):
        return Article.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.author_name = validated_data.get('author_name', instance.author_name)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.save()
        return instance
"""

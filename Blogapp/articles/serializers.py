from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):

    # define new fields or override/edit existing ones here
  
    slug = serializers.SlugField(read_only = True)
    author = serializers.StringRelatedField()
 
    class Meta:
        model = Article
        fields = '__all__'
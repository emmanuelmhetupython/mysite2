from rest_framework import serializers
from .models import Book
from .models import Post
from .models import TutorialCategory
from .models import TutorialSeries
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id','title','author','pdf','cover')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','title','post')
class TutiCateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutorialCategory
        fields = ('id','tutorial_category','category_summary','category_slug')
class TutorialSeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutorialSeries
        fields = ('id','tutorial_series','tutorial_category','series_summary')
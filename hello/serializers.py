from rest_framework import serializers
from .models import Product,Variants,Image,Options

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
class VariantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Variants
        fields = '__all__'
class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
class OptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Options
        fields = '__all__'

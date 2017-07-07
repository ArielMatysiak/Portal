from .models import Band, Photo, Region, City
from rest_framework import serializers


class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = "__all__"

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = "__all__"

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"


# class MovieSerializer(serializers.HyperlinkedModelSerializer):
#     director = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
#     actors = PersonSerializer(many=True)
#     class Meta:
#         model = Movie
#         fields = ('director', 'actors')

from classifieds.models import Band, Photo, Video, BandComments
from django.forms import ModelForm


class BandForm(ModelForm):

    class Meta:
        model = Band
        exclude = ["date"]


class PhotoForm(ModelForm):

    class Meta:
        model = Photo
        exclude = ["date"]

class VideoForm(ModelForm):

    class Meta:
        model = Video
        exclude = ["date"]

class BandCommentsForm(ModelForm):

    class Meta:
        model = BandComments
        exclude = '__all__'
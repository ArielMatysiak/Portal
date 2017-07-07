from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DeleteView
from classifieds.forms import BandForm, PhotoForm, VideoForm, BandCommentsForm
from classifieds.serializers import BandSerializer, PhotoSerializer, RegionSerializer, CitySerializer
from .models import Band, Photo, Video, BandComments, Region, TopicBand, MassageBand, City
from django.http import Http404
from django.shortcuts import render

from rest_framework import status
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView



class HomeView(View):
    def get(self, request):
        # bands = list(Band.objects.all())
        # bands = Band.objects.all()
        bands = Band.objects.order_by('?')
        bands_range = Band.objects.all()
        # bands = random.shuffle(bands)
        bands = list(bands)
        if len(bands) > 3:
            bands = bands[:4]
            # bands = random.shuffle(bands)[:4]

        photos = Photo.objects.order_by('?')
        # photos_range = Photo.objects.all()
        photos_range = Photo.objects.order_by('?')

        photos = list(photos)
        if len(photos) > 3:
            photos = photos[:4]

        # videos = Video.objects.all()
        videos = Video.objects.order_by('?')
        videos_range = Video.objects.all()
        videos = list(videos)
        if len(videos) > 3:
            videos = videos[:4]

        return render(request, "home.html",
                      {"bands": bands, "photos": photos, "videos": videos, "bands_range": bands_range,
                       "photos_range": photos_range, "videos_range": videos_range, })


class BandView(View):
    def get(self, request):
        # bands = Band.objects.all()
        bands = Band.objects.order_by('?')

        return render(request, "band.html", {"bands": bands})


class BandInfoView(View):

    def get_context(self, band, user):

        comments = BandComments.objects.filter(band=band)

        context = {"band": band,
                "regions": band.region.all(),
                "comments": comments
                }

        if user.is_authenticated:
            topic = TopicBand.objects.filter(band=band, user=user)
            if topic:
                topic = topic[0]
                context["massages_band"] = MassageBand.objects.filter(topic=topic)

        return context

    def get(self, request, pk):
        band = Band.objects.get(pk=pk)
        user = request.user

        return render(request, "band_info.html", self.get_context(band, user))

    def post(self, request, pk):
        band = Band.objects.get(pk=pk)
        user = request.user
        if request.POST["send"] == "massage":
            if user.is_authenticated:
                topic, created = TopicBand.objects.get_or_create(user=user, band=band)

                topic.save()

                mb = MassageBand(
                    massage_band=request.POST.get("massage_band",""),
                    topic=topic
                )
                try:
                    mb.save()
                except:
                    pass
            else:
                return redirect("/login")
        else:

            bc = BandComments(
                text=request.POST.get("text",""),
                author=request.POST.get("author","Gal Anonim"),
                band=band
            )
            try:
                bc.save()
            except:
                pass

        context = self.get_context(band, user)


        return render(request, 'band_info.html', context)


# class BandDelete(DeleteView):
#     model = Band
#     success_url = '/'
#
#     def get_success_url(self):
#         return "Zespół został usunięty"


class TestView(View):
    def get(self, request):
        return render(request, "test.html")


class AddBandView(View):
    def get(self, request):
        form = BandForm()
        ctx = {'form': form}

        return render(request, 'add_band.html', ctx)

    def post(self, request):

        form = BandForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/band")

        return render(request, 'add_band.html', {"form": form})


class PhotoView(View):
    def get(self, request):
        # photos = Photo.objects.all()
        photos = Photo.objects.order_by('?')
        return render(request, "photo.html", {"photos": photos})


class PhotoInfoView(View):
    def get(self, request, pk):
        photo = Photo.objects.get(pk=pk)

        return render(request, "photo_info.html", {"photo": photo,
                                                   "regions": photo.region.all()})


class AddPhotoView(View):
    def get(self, request):
        form = PhotoForm()
        ctx = {'form': form}

        return render(request, 'add_photo.html', ctx)

    def post(self, request):
        form = PhotoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/photo")

        return render(request, 'add_photo.html', {"form": form})


class VideoView(View):
    def get(self, request):
        # videos = Video.objects.all()
        videos = Video.objects.order_by('?')
        return render(request, "video.html", {"videos": videos})


class VideoInfoView(View):
    def get(self, request, pk):
        video = Video.objects.get(pk=pk)

        return render(request, "video_info.html", {"video": video,
                                                   "regions": video.region.all()})


class AddVideoView(View):
    def get(self, request):
        form = VideoForm()
        ctx = {'form': form}

        return render(request, 'add_video.html', ctx)

    def post(self, request):
        form = VideoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/video")

        return render(request, 'add_video.html', {"form": form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def get_user_profile(request, username):
    user = request.user
    if user.is_superuser or user.is_staff:
        user = User.objects.get(username=username)
    return render(request, 'user_profile.html', {"user":user})





class BandViewAPI(APIView):

    def get_object(self, pk):
        try:
            return Band.objects.get(pk=pk)
        except Band.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            band = self.get_object(pk)
            serializer = BandSerializer(band, context={"request": request})
            return Response(serializer.data)

        band = Band.objects.all()
        serializer = BandSerializer(band, many=True, context={"request": request})
        return Response(serializer.data)



    def delete(self, request, pk, format=None):
        band = self.get_object(pk)
        band.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    def put(self, request, pk, format=None):
        band = self.get_object(pk)
        serializer = BandSerializer(band, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def post(self, request, format=None):
        serializer = BandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PhotoViewAPI(APIView):

    def get_object(self, pk):
        try:
            return Photo.objects.get(pk=pk)
        except Photo.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            photo = self.get_object(pk)
            serializer = PhotoSerializer(photo, context={"request": request})
            return Response(serializer.data)

        movie = Photo.objects.all()
        serializer = PhotoSerializer(movie, many=True, context={"request": request})
        return Response(serializer.data)



    def delete(self, request, pk, format=None):
        photo = self.get_object(pk)
        photo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    def put(self, request, pk, format=None):
        photo = self.get_object(pk)
        serializer = PhotoSerializer(photo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def post(self, request, format=None):
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegionAPI(APIView):

    def get_object(self, pk):
        try:
            return Region.objects.get(pk=pk)
        except Region.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            name = self.get_object(pk)
            serializer = RegionSerializer(name, context={"request": request})
            return Response(serializer.data)

        name = Region.objects.all()
        serializer = RegionSerializer(name, many=True, context={"request": request})
        return Response(serializer.data)


class CityAPI(APIView):

    def get_object(self, pk):
        try:
            return City.objects.get(pk=pk)
        except Region.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            name = self.get_object(pk)
            serializer = CitySerializer(name, context={"request": request})
            return Response(serializer.data)

        name = City.objects.all()
        serializer = CitySerializer(name, many=True, context={"request": request})
        return Response(serializer.data)
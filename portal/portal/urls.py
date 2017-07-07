"""portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from classifieds.views import BandView, TestView, BandInfoView, AddBandView, PhotoView, PhotoInfoView ,AddPhotoView, VideoView, VideoInfoView, AddVideoView, HomeView, BandViewAPI, RegionAPI, signup, CityAPI, get_user_profile
from django.conf.urls.static import static
# from classifieds import settings
from portal import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name="home"),
    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^band/$', BandView.as_view(), name="band"),
    url(r'^band/(?P<pk>(\d)+)$', BandInfoView.as_view()),
    url(r'^add_band', AddBandView.as_view()),
    url(r'^test', TestView.as_view()),
    url(r'^photo/$', PhotoView.as_view(), name="photo"),
    url(r'^photo/(?P<pk>(\d)+)', PhotoInfoView.as_view()),
    url(r'^add_photo', AddPhotoView.as_view()),
    url(r'^video/$', VideoView.as_view(), name="video"),
    url(r'^video/(?P<pk>(\d)+)', VideoInfoView.as_view()),
    url(r'^add_video', AddVideoView.as_view()),
    url(r'^band/api', BandViewAPI.as_view()),
    url(r'^city/api', CityAPI.as_view()),

    url(r'^region/api', RegionAPI.as_view()),
    url(r'^signup/$', signup, name='signup'),
    url(r'profile/(?P<username>[a-zA-Z0-9]+)$', get_user_profile)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

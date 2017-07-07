from django.contrib import admin
from classifieds.models import Band, Region, Photo, Video, BandComments, City

admin.site.register(Band)
admin.site.register(Photo)
admin.site.register(Video)
admin.site.register(Region)
admin.site.register(City)
admin.site.register(BandComments)
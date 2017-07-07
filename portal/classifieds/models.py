from django.contrib.auth.models import User
from django.db import models

REGION = (
    (1, "mazowieckie"),
    (2, "śląskie"),
    (3, "wielkopolskie"),
    (4, "małopolskie"),
    (5, "dolnośląskie"),
    (6, "łódzkie"),
    (7, "pomorskie"),
    (8, "lubelskie"),
    (9, "podkarpackie"),
    (10, "kujawsko-pomorskie"),
    (11, "zachodniopomorskie"),
    (12, "warmińsko-mazurskie"),
    (13, "świętokrzyskie"),
    (14, "podlaskie"),
    (15, "lubuskie"),
    (16, "opolskie"),

)


# Create your models here.

class Region(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=64)
    region =  models.ForeignKey(Region)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ["region", "name"]


class Band(models.Model):
    band_name = models.CharField(max_length=124)
    image = models.ImageField(upload_to='images', null=True)
    number_of_people = models.SmallIntegerField(null=True)
    price = models.SmallIntegerField(null=True)
    region = models.ManyToManyField(Region)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return self.band_name

        return "{} Region: {} Cena: {}".format(self.band_name, ", ".join(self.region.values_list('name', flat=True)),
                                               self.price)


class Photo(models.Model):
    photo_name = models.CharField(max_length=124)
    image = models.ImageField(upload_to='images', null=True)
    number_of_people = models.SmallIntegerField(null=True)
    price = models.SmallIntegerField(null=True)
    region = models.ManyToManyField(Region)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return self.band_name

        return "{} Region: {} Cena: {}".format(self.photo_name, ", ".join(self.region.values_list('name', flat=True)),
                                               self.price)


class Video(models.Model):
    video_name = models.CharField(max_length=124)
    image = models.ImageField(upload_to='images', null=True)
    number_of_people = models.SmallIntegerField(null=True)
    price = models.SmallIntegerField(null=True)
    region = models.ManyToManyField(Region)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return self.band_name

        return "{} Region: {} Cena: {}".format(self.video_name, ", ".join(self.region.values_list('name', flat=True)),
                                               self.price)


class BandComments(models.Model):
    band = models.ForeignKey(Band)
    text = models.TextField(verbose_name='Komentarz')
    author = models.CharField(max_length=255, verbose_name='Autor', blank=True)


class TopicBand(models.Model):
    band = models.ForeignKey(Band)
    user = models.ForeignKey(User)


class MassageBand(models.Model):
    massage_band = models.TextField()
    topic = models.ForeignKey(TopicBand)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date']
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

class Brand(models.Model):
    name = models.TextField(max_length=100)
    photo = models.ImageField(upload_to='photo_brands/')
    rating = models.FloatField(default=5.0, null=True, blank=True)
    #cars

    def __str__(self):
        return self.name

    def url(self):
        return reverse('thecars:brand-detail', kwargs={'pk': self.id})

class Type(models.Model):
    name = models.TextField(max_length=100)
    photo = models.ImageField(upload_to='photo_types/')
    rating = models.FloatField(default=5.0, null=True, blank=True)
    #cars

    def url(self):
        return reverse('thecars:type-detail', kwargs={'pk': self.id})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-rating']


class Car(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photo_cars/')
    year = models.IntegerField(null=True, blank=True)
    rating = models.FloatField(default=5.0, null=True, blank=True)
    views = models.IntegerField(default=0, null=True, blank=True)
    price = models.IntegerField(default=1000, null=True, blank=True)
    review = models.CharField(max_length=12, null=True, blank=True)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, related_name='cars', null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, related_name='cars', null=True, blank=True)
    buy = models.TextField(null=True, blank=True)
    max_speed = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    # likes = models.ManyToManyField(User, related_name='likelist', blank=True)
    #comments

    def __str__(self):
        return self.name

    def url(self):
        return reverse('thecars:car-detail', kwargs={'slug': self.slug})

class UserAddon(models.Model):
    user = models.OneToOneField(User, related_name='addon', on_delete=models.CASCADE)
    userpic = models.ImageField(upload_to='userpics/', null=True, blank=True)

    def __str__(self):
        return f'{self.user}\'s addon'

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    text = models.TextField()
    published = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.text} ({self.car})'

    class Meta:
        ordering = ['-published']

# class LikeList(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likelist')
#     car = models.ManyToManyField(Car)
#
#     def __str__(self):
#         return f"{self.user}'s LikeList"





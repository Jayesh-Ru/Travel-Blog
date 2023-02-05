from django.db import models
from django.urls import reverse

# Create your models here.
class Country(models.Model):
    title = models.CharField(max_length=100, unique=True)
    desc1 = models.TextField(blank=True)
    img1 = models.ImageField(upload_to='photos')
    desc2 = models.TextField(blank=True)
    img2 = models.ImageField(upload_to='photos')
    population = models.BigIntegerField()
    cities = models.IntegerField()
    space = models.BigIntegerField()

    # def get_absolute_url(self):
    #     return reverse("store:category_list", args=[self.slug])

    def __str__(self):
        return self.title

class Destination(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=225, unique=True)
    image = models.ImageField(upload_to='photos')
    description = models.TextField(blank=True, null=True)
    country = models.ForeignKey(Country, related_name='destination', on_delete=models.CASCADE)

    class Meta:                                                       
        verbose_name_plural='destinations'
    
    def get_absolute_url(self):
        return reverse("travel_blog:destination_list", args=[self.slug])

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_destinations():
        return Destination.objects.all()

class DestinationDetail(models.Model):
    destination = models.ForeignKey(Destination, related_name='destination_detail', on_delete=models.CASCADE)

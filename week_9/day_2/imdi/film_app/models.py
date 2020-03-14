from django.db import models
# Create your models here.


class Country(models.Model):
    country_name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.country_name}'


class Category(models.Model):
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.category_name}'


class Director(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} and {self.last_name}'


class Film(models.Model):
    title = models.CharField(max_length=25)
    release_date = models.DateField() #auto_now_add=True
    country_name = models.ForeignKey(Country, on_delete=models.SET_NULL,null=True)
    category_name = models.ManyToManyField(Category)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL,null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'{self.title}'


class Comments(models.Model):
    film = models.ForeignKey(Film, on_delete=models.SET_NULL, null=True)
    comment = models.TextField(max_length=200, blank=True)

from django.db import models
from django.shortcuts import reverse
from django.contrib.admin.widgets import AdminDateWidget

# Create your models here.
ROOM_TYPE_CHOICES = (
    ('single', 'Single Room'),
    ('double', 'Double Room'),
    ('Executive', 'Executive Room'),
    ('Mini', 'Mini Suite'),
    ('presidential', 'Presidential Suite'),
    ('Deluxe', 'Deluxe Suite'),
    ('Twin', 'Twin Apartment'),

)
ADULT_CHOICE = [(i, i) for i in range(1, 4)]
CHILDREN_CHOICE = [(i, i) for i in range(0, 4)]


class Booking(models.Model):
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    room_type = models.CharField(max_length=20, choices=ROOM_TYPE_CHOICES, default='Single Room')
    check_in = models.DateField()
    check_out = models.DateField()
    adult = models.IntegerField(choices=ADULT_CHOICE, default=1)
    children = models.IntegerField(choices=CHILDREN_CHOICE, default=0)

    def __str__(self):
        return self.email + '-------' + self.room_type


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=500)
    message = models.TextField()

    def __str__(self):
        return self.name + '--------' + self.subject


class News(models.Model):
    title = models.CharField(max_length=250)
    published_date = models.DateField()
    reporter = models.CharField(max_length=40)
    content = models.TextField()
    slug = models.SlugField(null=True)
    picture = models.ImageField(upload_to='Pictures/News', null=True)

    def get_absolute_url(self):
        return reverse('blog-single', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=500)
    date = models.DateField(null=True)
    time_start = models.TimeField(null=True)
    time_end = models.TimeField(null=True)
    content = models.TextField()
    picture = models.ImageField(upload_to='Pictures/Event', null=True)

    def __str__(self):
        return self.title

from django.contrib import admin
from .models import Booking, News, Message, Event
from django.conf.locale.en import formats as en_formats

en_formats.DATE_FORMAT = "j F, Y"
# Register your models here.
admin.site.register(Booking)
admin.site.register(News)
admin.site.register(Message)
admin.site.register(Event)

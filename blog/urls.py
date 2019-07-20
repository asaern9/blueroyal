from django.urls import path
from . import views
from .views import BlogSingle
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('blog/', views.blog, name='blog-blog'),
    path('blog-single/<slug>/', BlogSingle.as_view(), name='blog-single'),
    path('contact/', views.contact, name='blog-contact'),
    path('rooms/', views.rooms, name='blog-room'),
    path('service/', views.services, name='blog-service'),

    # rooms
    path('deluxe-suite/', views.deluxe, name='room-deluxe'),
    path('double-room/', views.double, name='room-double'),
    path('executive-room/', views.executive, name='room-executive'),
    path('mini-suite/', views.mini, name='room-mini'),
    path('presidential-suite/', views.presidential, name='room-presidential'),
    path('single-room/', views.single, name='room-single'),
    path('twin-apartment/', views.twin, name='room-twin'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

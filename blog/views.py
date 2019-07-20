from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm, BookingForm
from .models import News, Event, Booking
from django.views.generic import DetailView
# Create your views here.


def index(request):
    event = Event.objects.all().order_by('-id')[:3]
    news = News.objects.all().order_by('-id')[:3]
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            print(form)
            form_save = form.save()
            return redirect('blog-home')
    else:
        form = BookingForm()
    return render(request, 'blog/index.html', {'form': form, 'event': event, 'news': news})


def about(request):
    return render(request, 'blog/about.html')


def blog(request):
    event = Event.objects.all().order_by('-id')
    news = News.objects.all().order_by('-id')
    context = {'event': event, 'news': news}
    return render(request, 'blog/blog.html', context)


class BlogSingle(DetailView):
    model = News
    template_name = 'blog/blog-single.html'


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form_save = form.save()
            return redirect('blog-contact')
    else:
        form = ContactForm()
    return render(request, 'blog/contact.html', {'form': form})


def rooms(request):
    return render(request, 'blog/rooms.html')


def services(request):
    return render(request, 'blog/services.html')


# rooms view
def deluxe(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form_save = form.save()
            return redirect('room-twin')
    else:
        form = BookingForm()
    return render(request, 'blog/room_deluxe.html', {'form': form})


def double(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form_save = form.save()
            return redirect('room-twin')
    else:
        form = BookingForm()
    return render(request, 'blog/room_double.html', {'form': form})


def executive(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form_save = form.save()
            return redirect('room-twin')
    else:
        form = BookingForm()
    return render(request, 'blog/room_executive.html', {'form': form})


def mini(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form_save = form.save()
            return redirect('room-twin')
    else:
        form = BookingForm()
    return render(request, 'blog/room_mini.html', {'form': form})


def presidential(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form_save = form.save()
            return redirect('room-twin')
    else:
        form = BookingForm()
    return render(request, 'blog/room_presidential.html', {'form': form})


def single(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form_save = form.save()
            return redirect('room-twin')
    else:
        form = BookingForm()
    return render(request, 'blog/room_single.html', {'form': form})


def twin(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form_save = form.save()
            return redirect('room-twin')
    else:
        form = BookingForm()
    return render(request, 'blog/room_twin.html', {'form': form})

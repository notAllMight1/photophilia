from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from .models import Photo, Comment, Like
from .forms import PhotoForm, CommentForm

def index(request):
    featured_photos = Photo.objects.order_by('-uploaded_at')[:6]  # Display the latest 6 photos
    return render(request, 'index.html', {'featured_photos': featured_photos})

def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'gallery.html', {'photos': photos})

def photo_detail(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    comments = photo.comments.all()
    liked = False
    if request.user.is_authenticated:
        liked = Like.objects.filter(photo=photo, user=request.user).exists()
    return render(request, 'gallery_single.html', {
        'photo': photo, 'comments': comments, 'liked': liked
    })

@login_required
def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.uploaded_by = request.user
            photo.save()
            return redirect('photo_list')
    else:
        form = PhotoForm()
    return render(request, 'upload_photo.html', {'form': form})

@login_required
def like_photo(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    if Like.objects.filter(photo=photo, user=request.user).exists():
        Like.objects.filter(photo=photo, user=request.user).delete()  # Unlike if already liked
    else:
        Like.objects.create(photo=photo, user=request.user)  # Like the photo
    return redirect('photo_detail', photo_id=photo.id)

@login_required
def add_comment(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.photo = photo
            comment.author = request.user
            comment.save()
            return redirect('photo_detail', photo_id=photo.id)
    return HttpResponseForbidden()

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')
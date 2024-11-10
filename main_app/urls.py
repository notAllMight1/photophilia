from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("gallery/", views.photo_list, name="photo_list"),
    path("photo/<int:photo_id>/", views.photo_detail, name="photo_detail"),
    path("upload/", views.upload_photo, name="upload_photo"),
    path("like/<int:photo_id>/", views.like_photo, name="like_photo"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_view, name="logout"),
]

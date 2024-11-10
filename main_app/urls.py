from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("gallery/", views.photo_list, name="photo_list"),
    path("photo/<int:photo_id>/", views.photo_detail, name="photo_detail"),
    path("upload/", views.upload_photo, name="upload_photo"),
    path("like/<int:photo_id>/", views.like_photo, name="like_photo"),
    path("comment/<int:photo_id>/", views.add_comment, name="add_comment"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("user/uploads/", views.user_uploads, name="user_uploads"),
    path('user/uploads/photo/edit/<int:photo_id>/', views.edit_caption, name='edit_caption'),
    path('user/uploads/photo/delete/<int:photo_id>/', views.photo_delete, name='photo_delete'),

]

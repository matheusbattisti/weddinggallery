from django.urls import path

from . import views

urlpatterns = [
    path('', views.GalleryView, name="gallery"),
    path('myphotos', views.MyPhotosView, name="myphotos"),
    path('approvephotos', views.ApprovePhotosView, name="approvephotos"),
    path('approve/', views.ApproveView, name="approve"),
    path('like/', views.LikeView, name="like"),
    path('upload', views.UploadView, name="upload"),
]
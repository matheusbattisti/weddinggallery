from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Photo, Like

from .forms import PhotoForm

from . import functions

@login_required
def GalleryView(request):

    order_by = request.GET.get('order_by', '')
    current_user = request.user
    user_id = current_user.id

    if(order_by == 'latest'):
        order_by = '-date_taken'
    elif(order_by == 'oldest'):
        order_by = 'date_taken'
    elif(order_by == 'mostlikes'):
        order_by = '-like_count'
    elif(order_by == 'lesslikes'):
        order_by = 'like_count'
    else:
        order_by = '-date_taken'

    photos = Photo.objects.filter(approved='yes').order_by(order_by)

    likes = Like.objects.all()

    functions.getLikedPhotos(user_id, photos, likes)

    return render(request, 'gallery/gallery.html', {'photos': photos, 'order_by': order_by})

@login_required
def MyPhotosView(request):
    current_user = request.user
    user_id = current_user.id
    
    photos = Photo.objects.filter(author=user_id).order_by('-created_at')
    likes = Like.objects.all()

    functions.getLikedPhotos(user_id, photos, likes)

    return render(request, 'gallery/myphotos.html', {'photos': photos})

@login_required
def ApprovePhotosView(request):
    
    photos = Photo.objects.filter(approved='no').order_by('-created_at')

    return render(request, 'gallery/approve.html', {'photos': photos})
    
@login_required
def ApproveView(request):
    photo_id = request.GET.get('photo_id')

    photo = get_object_or_404(Photo, pk=photo_id)
    photo.approved = 'yes'
    photo.save()

    messages.add_message(request, messages.SUCCESS, 'The photo has been approved.')

    return redirect('gallery')



@login_required
def UploadView(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            photo = form.save(commit=False)
            photo.author = request.user
            photo.approved = 'no'
            photo.save()
            return redirect('myphotos')
        else:
            return render(request, 'gallery/upload.html', {'form': form})

    else:
        form = PhotoForm()
        return render(request, 'gallery/upload.html', {'form': form})

@login_required
def LikeView(request):
    likeType = request.GET.get('liketype')
    photo_id = request.GET.get('photo_id')

    photo = get_object_or_404(Photo, pk=photo_id)
    current_user = request.user
    user_id = current_user.id
    current_like_count = photo.like_count

    if(likeType == 'dislike'):
        photo.like_count = current_like_count - 1
        photo.save()
        like = Like.objects.get(photo_id=photo_id, author_id=user_id)
        like.delete()
        messages.add_message(request, messages.SUCCESS, 'You have sucessfully unliked this photo.')
        return redirect('gallery')
    else:
        photo.like_count = current_like_count + 1
        photo.save()
        like = Like(author=request.user, photo=photo)
        like.save()
        messages.add_message(request, messages.SUCCESS, 'You have sucessfully liked this photo.')
        return redirect('gallery')
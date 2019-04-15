def getLikedPhotos(user_id, photos, likes):
    for photo in photos:
        for like in likes:
            if photo.id == like.photo_id and user_id == like.author_id:
                photo.liked = 'yes'
                break
            else:
                photo.liked = 'no'
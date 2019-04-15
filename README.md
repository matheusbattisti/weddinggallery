# weddinggallery
A Wedding Gallery Project.

1 - Requirements:
    - Python 3.6.4
    - MongoDb 4.0.5
    - Django 2.2;
    - pip
    - django-crispy-forms 1.7.2
    - django-debug-toolbar 1.11
    - django-storages 1.7.1
    - djongo 1.2.32
    - boto3 1.9.130
    - Pillow 5.1.0

2 - How to run this application:
    - Install MongoDB
    - Check if you have pip installed - sudo pip3 --version
    - If dont install it with - sudo apt-get install python3-pip
    - Install virtualenv with - sudo pip3 install virtualenv 
    - Create a venv - virtualenv venv
    - Activate the venv - source venv/bin/activate
    - Install the dependencies listed in requirements with pip - pip3 install django
    - Create a .env file at the root of application with these constants and their respective values:
        AWS_ACCESS_KEY_ID'
        AWS_SECRET_ACCESS_KEY
        ALLOWED_HOSTS
        DEBUG
        SECRET_KEY
        DB_HOST
        DB_NAME
    - Make migrations - python manage.py makemigrations
    - Migrate - python manage.py migrate
    - Create a super user to access the admin - python manage.py createsuperuser
    - Run the server - python manage.py runserver

3 - About the application design:

    I've based this application on three models: Photo, Like and User

    Where Photo contains a title, src, date taken, like count and approval status, the title is a simple description for the images, the src is the path to the file, date taken is used to sort the gallery were you can choose the oldests or newests, like count is updated when users like or dislikes images and is used to sort for the most and the less liked images, and all uploaded images have a status of 'no' wich means they arent showed in the gallery, and only the groom and the bride can change this.

    The Like model contains two foreign keys one for the User and the other for the Photo, so its not possible to like twice the same photo because the application check if the user has already liked it, and it is also possible to dislike photos if they were liked before.

    And the User models is an extended version of User Django Model, I just added a field to check if the User is a guest of the wedding or no, if he is not a guest he can approve the images to be shown in the gallery, this status can only be updated by an admin. 

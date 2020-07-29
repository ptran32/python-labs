# Created manually

""" Define URL's pattern for learning_logs. """

from django.urls import path, include


from . import views




app_name = "users" # Namespace name
urlpatterns = [
    # Include default auth url
    # Built-in url patterns such as /users/login
    # Django will use a default view function
    # but need to create a view where to send it. the default is looking for a template in a folder called "registration"
    path('', include('django.contrib.auth.urls')),
    # New registration for new users
    path('register/', views.register, name='register'),
]
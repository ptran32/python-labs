# Created manually

""" Define URL's pattern for learning_logs. """

from django.urls import path

from . import views

# helps django distinguish urls.py from other app with the same urls.py
app_name = "learning_logs" # Namespace name
urlpatterns = [
    # Home Page
    # #named_url is index. Used as reference in templates (index.html) learning_logs:index
    path('', views.index, name='index'), 
    # Page that show all topics
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic
    path('topic/<int:topic_id>/', views.topic, name='topic'),
    # Page for adding new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'), # register int as var for topic_id
    # Page for editing an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry') # register in as var for entry_id
]
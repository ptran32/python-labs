from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .forms import TopicForm, EntryForm
from .models import Topic, Entry


def check_topic_owner(request, topic_id):
    """ Verify if a user is the owner of a topic
        return 404 code if not """
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404


def index(request):
    """ The home page for learning log """
    return render(request, 'learning_logs/index.html')

# Decorator check if user is logged in, if not, redirect to loggin page
# Login page is set with LOGIN_URL in settings.py
@login_required
def topics(request): # request object Django received from the server
    """ Display all toppics """
    # When logged-in, request has a user attribute that store infos about him
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    # Context is a dictionnary where. Key's name is use in template to access datas
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context) # send context as well to be render

@login_required
def topic(request, topic_id): # topic_id comes from urls.py
    """ Display a single topic and all it's entries """
    check_topic_owner(request, topic_id)

    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added') # the dash sort the result in reverse order
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """ Display a new topic """
    # Return empty form if no data submitted
    if request.method != "POST":
        form = TopicForm()
    else:
        # Post data submitter, process data
        form = TopicForm(data=request.POST)
        if form.is_valid(): # Check the post is validß
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics') # Redirect user's browser to the topic page

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """ Add a new entry """
    topic = Topic.objects.get(id=topic_id)
    # No data submit -> return empty form
    if request.method != "POST":
        form = EntryForm()
    else:
        # Post data submitter, process data
        form = EntryForm(data=request.POST)
        if form.is_valid(): # Check the post is valid
            new_entry = form.save(commit=False)
            new_entry.topic = topic # Add a new attribute here, there were None before.
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id) # Redirect user's browser to the topic page. # topic_id from parameter

    # Display a blank or invalid form
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """ Edit an existing entry """
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    topic_id = topic.id

    check_topic_owner(request, topic_id)

    if request.method != 'POST':
        # Initial request, pre-fill for with the current entry
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            print('ok')
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)  # Redirect user's browser to the topic page

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

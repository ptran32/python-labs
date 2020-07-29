from django.db import models
from  django.contrib.auth.models import User

class Topic(models.Model):
    """ A Topic the user is learning about """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    # When migrating, we need to put a userID to link all Topic to admin for now;.
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """ Return a string representation of the model """
        return self.text

class Entry(models.Model):
    """ Something specific learned about a topic """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) # Many to one relaitionship - May entries can be associated with one topic
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Meta class hold extra informations about a model 
            It allow us to set a special attribute telling Django to use
            Entries when it needs to refer to more than one entry"""

        verbose_name_plural = 'entries'


    def __str__(self):
        """ Return a string representation of the model """
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return self.text

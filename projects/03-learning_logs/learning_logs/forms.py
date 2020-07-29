from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text'] # Include a text field from the models
        labels = {'text': ''} # Do not generate a label. Label display a text near the field.

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry:'}
        # Override Djanfo default here.
        # a widget is an html form element, such as signe line text box, multi line area text or drop down list
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

from django import forms
from .models import Topic, Post


# class oriented form of a new topic
class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(), max_length=4000)

    class Meta:
        model = Topic
        fields = ['subject', 'message']



class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', ]



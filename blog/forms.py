from django import forms
from .models import Comment
from .models import Message


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "email", "message"]


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["name", "email", "message"]

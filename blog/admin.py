from django.contrib import admin
from .models import Post
from .forms import Comment
from .forms import Message

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Message)

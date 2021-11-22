from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['text', 'group', 'image']
        help_text = {
            'text': 'Текст нового поста',
            'group': 'Группа, к которой будет относиться пост',
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']
        help_text = {
            'text': 'Текст комментария',
        }

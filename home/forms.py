from django.forms import ModelForm, Textarea, TextInput, FileInput
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["image", "title", "content"]
        widgets = {
            "image": FileInput(attrs={
                "style": "margin: 20px; width: 1190px;",
                "class": "form-control",
                "type": "file",
                "placeholder": "Изображение",
                }),
            "title": TextInput(attrs={
                "style": "margin: 20px; width: 1190px;",
                "class": "form-control",
                "type": "text",
                "placeholder": "Заголовок",
            }),
            "content": Textarea(attrs={
                "style": "margin: 20px; width: 1190px;",
                "class": "form-control",
                "type": "text",
                "placeholder": "Описание",
                "cols": "30",
                "rows": "10",
            }),
        }
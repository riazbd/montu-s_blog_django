from django import forms
from django.core.exceptions import ValidationError
from .models import Post, Comment, Category

choices = Category.objects.all().values_list("name", "name")

choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "author", "image", "category", "body")

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.Select(attrs={"class": "form-control"}),
            "category": forms.Select(
                choices=choice_list, attrs={"class": "form-control"}
            ),
            "body": forms.Textarea(attrs={"class": "form-control"}),
        }


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "image", "body")

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "comment"]

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "comment": forms.Textarea(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        """Save the request with the form so it can be accessed in clean_*()"""
        self.request = kwargs.pop("request", None)
        super(CommentForm, self).__init__(*args, **kwargs)

    def clean_name(self):
        """Make sure people don't use my name"""
        data = self.cleaned_data["name"]
        if not self.request.user.is_authenticated and data.lower().strip() == "admin":
            raise ValidationError("Sorry, you cannot use this name.")
        return data

from django import forms
from authors.models import Author
from .models import BookTitle
from django.core.exceptions import ValidationError


class BookTitleForm(forms.ModelForm):
    class Meta:
        model = BookTitle
        fields = ('title', 'author', 'publisher')

    def clean(self):
        title = self.cleaned_data.get('title')

        if len(title) < 5:
            error_msg = 'Sorry, but the title is too short.'
            self.add_error('title', error_msg)

        book_title_exists = BookTitle.objects.filter(title__iexact=title).exists()

        if book_title_exists:
            self.add_error('title', 'This title already exists in the database.')

        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].queryset = Author.objects.all()
        self.fields['author'].label_from_instance = lambda obj: obj.formatted_name



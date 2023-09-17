from django import forms
from authors.models import Author



class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'birth_year')

    def clean(self):
        name = self.cleaned_data.get('name')

        if len(name) < 1:
            error_msg = 'Sorry, but the title is too short.'
            self.add_error('name', error_msg)

        author_name_exists = Author.objects.filter(name__iexact=name).exists()

        if author_name_exists:
            self.add_error('name', 'This title already exists in the database.')

        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

from django import forms
from publishers.models import Publisher





class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ('name', 'country','headquarters','founded')

    def clean(self):
        name = self.cleaned_data.get('name')

        if len(name) < 1:
            error_msg = 'Sorry, but this name is too short.'
            self.add_error('name', error_msg)

        author_name_exists = Publisher.objects.filter(name__iexact=name).exists()

        if author_name_exists:
            self.add_error('name', 'This publisher already exists in the database.')

        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

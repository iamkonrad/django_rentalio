from django import forms

from rentals.choices import FORMAT_CHOICES


class SearchBookForm(forms.Form):
    search = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Type book id or ISBN here and press ENTER    ','id':'custom_id'}))

class SelectExportOptionForm(forms.Form):
    format=forms.ChoiceField(choices=FORMAT_CHOICES, widget=forms.RadioSelect)


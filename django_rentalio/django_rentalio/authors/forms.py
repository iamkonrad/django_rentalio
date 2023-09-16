from django import forms




class SearchAuthorForm(forms.Form):
    search = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Insert authors name here and press ENTER    ','id':'custom_id'}))
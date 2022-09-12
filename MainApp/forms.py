from django.forms import ModelForm, TextInput, Textarea, Select
from MainApp.models import Snippet


class SnippetForm(ModelForm):
   class Meta:
       model = Snippet
       # Описываем поля, которые будем заполнять в форме
       fields = ['name', 'lang', 'code']
       widgets = {
           'name': TextInput(attrs={'class':'form-control form-control-md','placeholder': 'Название виджета'}),
           'lang': Select(attrs={'class': 'form-control form-control-md', 'placeholder': 'Язык программирования'}),
           'code': Textarea(attrs={'class': 'form-control form-control-md', 'placeholder': 'Код'}),
       }
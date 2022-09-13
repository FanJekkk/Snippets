from django.forms import ModelForm, TextInput, Textarea, Select, CheckboxInput, CharField, PasswordInput, ValidationError
from MainApp.models import Snippet
from django.contrib.auth.models import User


class SnippetForm(ModelForm):
   class Meta:
       model = Snippet
       # Описываем поля, которые будем заполнять в форме
       fields = ['name', 'lang', 'code','hidden']
       widgets = {
           'name': TextInput(attrs={'class':'form-control form-control-md','placeholder': 'Название'}),
           'lang': Select(attrs={'class': 'form-control form-control-md', 'placeholder': 'Язык программирования'}),
           'code': Textarea(attrs={'class': 'form-control form-control-md', 'placeholder': 'Код'}),
           'hidden': CheckboxInput(attrs={'class': 'form-control form-control-md'})

       }

class UserRegistrationForm(ModelForm):
   class Meta:
       model = User
       fields = ["username", "email"]
       widgets = {
           'username': TextInput(attrs={"class": "form-control form-control-md"}),
           'email': TextInput(attrs={"class": "form-control form-control-md"}),
       }
   password1 = CharField(label="Password", widget=PasswordInput(attrs={"class": "form-control form-control-md"}))
   password2 = CharField(label="Password confirm", widget=PasswordInput(attrs={"class": "form-control form-control-md"}))

   def clean_password2(self):
       pass1 = self.cleaned_data.get("password1")
       pass2 = self.cleaned_data.get("password2")
       if pass1 and pass2 and pass1 == pass2:
           return pass2
       raise ValidationError("Пароли не совпадают или пустые")

   def save(self, commit=True):
       user = super().save(commit=False)
       user.set_password(self.cleaned_data["password1"])
       if commit:
           user.save()
       return user
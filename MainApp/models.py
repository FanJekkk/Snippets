from django.db import models
from django.contrib.auth.models import User

LANGS = [
    ("Python", "Python"),
    ("Javascript", "JavaScript"),
    ("C++",  "C++"),
]

PARAM = [
    ("Публичный", "Публичный"),
    ("Частный", "Частный"),
]

class Snippet(models.Model):
    name = models.CharField(max_length=100,default="")
    lang = models.CharField(max_length=30, choices=LANGS)
    code = models.TextField(max_length=5000,default="")
    creation_date = models.DateTimeField(auto_now_add=True)
    parametr = models.CharField(max_length=30, choices=PARAM)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE,
                             blank=True, null=True, related_name="snippets")
    def __str__(self):
        return f"Snippet: {self.name} Author: {self.user}"

class Comment(models.Model):
   comment = models.CharField(max_length=5000,default="")
   creation_date = models.DateTimeField(auto_now_add=True)
   author = models.ForeignKey(to=User, on_delete=models.CASCADE,
                              related_name="comments")
   snippet = models.ForeignKey(to=Snippet, on_delete=models.CASCADE,
                               related_name="comments")
   image = models.ImageField(upload_to="images",default="")


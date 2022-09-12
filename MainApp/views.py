from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from MainApp.forms import SnippetForm


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    if request.method == "GET":
        form = SnippetForm()
        context = {'pagename': 'Добавление нового сниппета', 'form': form}
        return render(request, 'pages/add_snippet.html', context)
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("snippets")
        return render(request, 'add_snippet.html', {'form': form})


def snippets_page(request):
    snippets = Snippet.objects.all()
    context = {'snippets': snippets}
    return render(request, 'pages/view_snippets.html', context)

def snippet(request, id):
    snippets = Snippet.objects.filter(pk=id)
    context = {'pagename': 'Описание', 'snippets': snippets}
    return render(request, 'pages/snippet_details.html', context)

def del_snippet_page(request, id):
    snippets = Snippet.objects.filter(id=id)
    snippets.delete()
    return redirect("snippets")